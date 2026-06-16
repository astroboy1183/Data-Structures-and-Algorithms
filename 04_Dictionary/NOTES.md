# Dictionaries — Learning Notes

A **dictionary** (`dict`) stores data as **key → value** pairs. Comprehensive notes
built from the code in this folder, with examples, complexity, and the common gotchas.
Each section points to the script(s) it comes from.

---

## 0. What is a dictionary?

- Maps unique **keys** to **values**: `{"name": "Jayanth", "age": 27}`.
- **Mutable** — you can add, change, and remove pairs in place.
- **Keys** must be **unique** and **hashable** (immutable types: `str`, `int`, `float`,
  `bool`, `tuple` — **not** `list` or `dict`). **Values** can be *any* type.
- **Ordered** — since Python 3.7 a dict keeps **insertion order**.
- Built on a **hash table**, so looking up / inserting / deleting **by key is O(1)** on average.

---

## 1. Creating dictionaries — `01_dictionary.py`

| Way | Example | Result |
|-----|---------|--------|
| Empty | `dict()` or `{}` | `{}` |
| Literal | `{"key1": "value1"}` | from `key: value` pairs |
| Keyword args | `dict(key1="value1")` | keys become strings |
| From a list of tuples | `dict([("a", 1), ("b", 2)])` | `{'a': 1, 'b': 2}` |
| From two lists (zip) | `dict(zip(keys, values, strict=True))` | pairs them up |
| `fromkeys()` | `dict.fromkeys(["a", "b"], 0)` | every key shares one default value |

- **Quotes are only for strings** — keys/values that are numbers, lists, dicts, `True`/`None`
  go in without quotes. Values can be mixed types.

## 2. Accessing values — `02`, `03_dictionary.py`

| Way | Missing key |
|-----|-------------|
| `d[key]` | raises **`KeyError`** |
| `d.get(key)` | returns `None` |
| `d.get(key, default)` | returns `default` |

Use `get()` whenever a key might be absent and you don't want a crash.

## 3. Adding & updating — `02`, `03_dictionary.py`

- `d[key] = value` — adds the key (or overwrites it if it exists). **Never** raises for a new key.
- `d.update(other)` — merge another dict/pairs in: overwrite matching keys, add new ones.
- `d1 | d2` — a **new** merged dict (Python 3.9+); on a clash the **right** side wins.
- `d |= other` — in-place merge (same effect as `update`).
- `d.setdefault(key, default)` — return the key's value, **inserting** `key: default` if absent.

## 4. Removing — `02`, `03_dictionary.py`

| Operation | Removes | Returns? |
|-----------|---------|----------|
| `d.pop(key)` | that key | the value (or `KeyError`) |
| `d.pop(key, default)` | that key | the value, or `default` if absent (no error) |
| `d.popitem()` | the **last inserted** pair | the `(key, value)` tuple |
| `del d[key]` | that key | — (`KeyError` if absent) |
| `d.clear()` | **everything** | — (`{}`) |

## 5. Iterating & view objects — `01`, `02`, `03_dictionary.py`

- `for key in d:` — iterating a dict yields its **keys**.
- `for key, value in d.items():` — the clean way to get **both** at once.
- **Views:** `d.keys()`, `d.values()`, `d.items()` return live `dict_keys` / `dict_values` /
  `dict_items` objects. Wrap in `list(...)` to get a plain list (e.g. `list(d.items())`
  → `[('a', 1), ('b', 2)]`).

## 6. Membership, length, queries — `04_dictionary.py`

- `key in d` → checks the **keys** (fast, O(1)). `value in d.values()` → checks values (O(n)).
- `len(d)` → number of pairs.
- `all(d)` / `any(d)` / `sorted(d)` → operate on the **keys** (e.g. `all` is `False` if any key
  is falsy like `0`/`False`).
- `d1 == d2` → equal if they have the **same key-value pairs** (insertion order doesn't matter).

## 7. Nested dictionaries — `02_dictionary.py`

- A value can itself be a dict: `people = {"p1": {"name": "Jayanth", "city": "Mumbai"}}`.
- Reach inner values by **chaining keys**: `people["p1"]["city"]` → `"Mumbai"`.

## 8. Dictionary comprehensions — `05_dictionary.py`

```python
{city: randint(20, 30) for city in cities}             # build
{c: t for c, t in temps.items() if t > 25}             # build + filter
```

## 9. Common patterns

- **Counting frequencies** (`03_dictionary.py`): `counts[x] = counts.get(x, 0) + 1`.
- **Sort by value** (`04_dictionary.py`): `sorted(d.items(), key=lambda kv: kv[1])`,
  then `dict(...)` to rebuild an ordered dict.
- **Merge & sum common keys** (`05_dictionary.py`): loop both dicts, summing where keys overlap.

## 10. Keys must be hashable — `01_dictionary.py`

- `{("x", "y"): "ok"}` works (a tuple is hashable).
- `{["x", "y"]: "no"}` → `TypeError: unhashable type: 'list'` (lists can't be keys).

---

## 11. Time complexity (`n` = number of pairs)

| Operation | Time |
|-----------|------|
| Access / insert / update / delete **by key** | O(1) average |
| `key in d` (membership on keys) | O(1) average |
| `value in d.values()` | O(n) |
| `len(d)` | O(1) |
| Iterating keys / values / items | O(n) |
| `copy()` | O(n) |
| Building from / converting to a list | O(n) |

> Worst case for key operations is O(n) (many hash collisions), but that's rare in practice.

## 12. Space complexity

- Storing the dictionary: **O(n)**.
- A dict carries extra overhead vs a list/tuple (it stores hashes + keys + values), so it
  trades memory for fast key lookups.

---

## Gotchas cheat-sheet

- **`d[missing]` raises `KeyError`** — use `d.get(key)` / `d.get(key, default)` to be safe.
- **`in` checks keys, not values** — for values use `value in d.values()`.
- **`all`/`any`/`sorted` work on keys**, so a falsy key (`0`, `False`) affects `all`.
- **Shallow vs deep copy:** `d.copy()` copies the outer dict but **shares** nested
  dicts/lists; use `copy.deepcopy(d)` for fully independent nested data.
- **Don't add/remove keys while iterating** a dict — it raises
  `RuntimeError: dictionary changed size during iteration`. Iterate over `list(d)` if you must modify.
- **`update` / `d[k] = v` never error on new keys** — only *reading* or *popping* a missing key complains.
