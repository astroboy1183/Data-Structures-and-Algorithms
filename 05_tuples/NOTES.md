# Tuples — Learning Notes

A **tuple** is an **ordered, immutable** sequence: `(1, 2, 3)`. Comprehensive notes built
from the code in this folder, with examples, complexity, and the common gotchas.
Each section points to the script(s) it comes from.

---

## 0. What is a tuple?

- An **ordered** collection, written with parentheses: `(1, 2, 3)`.
- **Immutable** — once created, you **cannot** change, add, or remove elements.
- Can hold **mixed types** and **duplicates**: `(1, "a", 1, 3.0)`.
- **Hashable** (if all its items are hashable) — so a tuple can be a **dict key** or a **set member**.
- Indexing is **O(1)**; it stores values compactly (a bit lighter than a list).

Think of a tuple as a **fixed record** — a group of values that belong together and shouldn't change.

---

## 1. Creating tuples — `01_tuples.py`

| Way | Example | Result |
|-----|---------|--------|
| Literal | `(1, 2, 3, 4)` | a 4-element tuple |
| **Single element** | `(2,)` | the trailing comma is **required** |
| Not a tuple! | `(2)` | just the integer `2` |
| Empty | `()` | empty tuple |
| From a string | `tuple("abcdef")` | `('a', 'b', 'c', 'd', 'e', 'f')` |
| From a list | `tuple([1, 2, 3, 4])` | `(1, 2, 3, 4)` |

> ⚠️ The single-element gotcha: `(5)` is the number 5; `(5,)` is a one-item tuple. The
> **comma** makes the tuple, not the parentheses.

## 2. Indexing & slicing — `01_tuples.py`

Works exactly like lists/strings (tuples are sequences):
- **Index:** `t[1]` (positive), `t[-1]` (last).
- **Slice:** `t[3:6]`, `t[:3]`, `t[:-1]` — returns a **new tuple**.
- **Step (incl. negative):** `t[::-1]` (reversed), `t[:3:-2]`, `t[:-1:-3]`.

## 3. Traversal — `01_tuples.py`

```python
for x in my_tuple:            # iterate the items directly
    ...
for i in range(len(my_tuple)):  # iterate by index
    print(my_tuple[i])
```

## 4. Operators — `01`, `02_tuples.py`

- `t1 + t2` → **concatenation** (a new tuple).
- `t * 3` → **repetition** (a new tuple).
- `x in t` / `x not in t` → membership test (O(n)).

(Like lists, `+` joins and `*` repeats — they don't do element-wise math.)

## 5. Methods — tuples have only TWO — `01`, `02_tuples.py`

Because they're immutable, tuples expose just two methods (no `append`/`remove`/`sort`/etc.):

| Method | Purpose |
|--------|---------|
| `t.count(x)` | how many times `x` appears |
| `t.index(x)` | the **first** position of `x` (raises `ValueError` if absent) |

- **All positions of a value** (since `index` only finds the first):
  ```python
  indices = [i for i, value in enumerate(t) if value == 1]
  ```

## 6. List vs tuple — `03_tuples.py`

| | `list` | `tuple` |
|--|--------|---------|
| Written with | `[ ]` | `( )` |
| Mutable? | ✅ yes | ❌ no (immutable) |
| Methods | many (`append`, `sort`, …) | only `count`, `index` |
| Hashable (dict key / set item)? | ❌ no | ✅ yes (if items are hashable) |
| Memory | larger | smaller |
| Indexing, slicing, `len`, `in`, `+`, `*` | ✅ | ✅ (same) |

- Changing a tuple item → `TypeError: 'tuple' object does not support item assignment`.
- `tuple.append(...)` → `AttributeError: 'tuple' object has no attribute 'append'`.
- A **list** key → `TypeError: unhashable type: 'list'`; a **tuple** key is fine.

## 7. When to use a tuple

- **Fixed records** that shouldn't change — coordinates `(x, y)`, RGB `(r, g, b)`, a date `(y, m, d)`.
- **Dictionary keys / set members** (lists can't be used there).
- **Returning multiple values** from a function (`return a, b` is really returning a tuple).
- When you want a **safe, read-only** sequence (immutability prevents accidental edits).

## 8. Tuple unpacking (a key feature)

```python
point = (3, 4)
x, y = point             # x = 3, y = 4
a, b = b, a              # swap with no temp variable
first, *rest = (1, 2, 3) # first = 1, rest = [2, 3]
```

## 9. Immutability nuance (important gotcha)

A tuple is immutable, but that only fixes **which objects** it holds — if one of those
objects is itself **mutable** (e.g. a list), that object can still change:

```python
t = (1, [2, 3])
t[1].append(4)     # allowed! the list inside the tuple is mutable
# t is now (1, [2, 3, 4])
t[1] = [9]         # NOT allowed -> TypeError (can't rebind the tuple slot)
```

---

## 10. Time complexity (`n` = number of items)

| Operation | Time |
|-----------|------|
| Access by index `t[i]` | O(1) |
| `len(t)` | O(1) |
| Search: `x in t`, `t.index(x)`, `t.count(x)` | O(n) |
| Slice of `k` items | O(k) (new tuple) |
| Concatenate `t1 + t2` | O(n + m) (new tuple) |
| Iterate | O(n) |

> There's no insert/delete — tuples are immutable. "Changing" one really means building a
> new tuple (e.g. via slicing/concatenation), which is O(n).

## 11. Space complexity

- Storing the tuple: **O(n)**.
- A tuple uses **less memory** than an equivalent list (no spare capacity for growth) — e.g.
  `(1, 2, 3)` is smaller than `[1, 2, 3]` (`03_tuples.py` shows this with `sys.getsizeof`).

---

## Gotchas cheat-sheet

- **One-element tuple needs a comma:** `(5,)`, not `(5)`.
- **Tuples are immutable** — no item assignment, no `append`/`sort`; "editing" means making a new tuple.
- **But mutable items inside can still change** (the list-inside-a-tuple case above).
- **`index()` finds only the first match** — use the `enumerate` comprehension for all positions.
- **Use tuples for fixed data and as dict keys/set items**; use lists when you need to change contents.
