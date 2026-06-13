# Lists — Learning Notes

Comprehensive notes on Python lists, built from the code in this folder.
Each section maps to the script(s) where the idea appears, with examples,
complexity, and the common gotchas. Use it to learn or to revise quickly.

---

## 0. What is a list?

- A **list** is Python's built-in, general-purpose sequence: `[1, "a", 3.0]`.
- **Ordered** — items keep their position and are accessed by index.
- **Mutable** — you can change, add, and remove items in place.
- **Heterogeneous** — items can be of mixed types (numbers, strings, even other lists).
- **Dynamic array under the hood** — it grows/shrinks automatically and stores
  **references** to objects (not the raw values), which is why it can hold mixed types.
- Indexing is **O(1)**; it over-allocates spare capacity so `append` is *amortized* O(1).

---

## 1. Creating lists & types — `01_lists.py`

```python
integers   = [1, 2, 3, 4]                       # numbers
stringList = ["apple", "banana", "cherry"]      # strings
mixedList  = [1, "apple", 2, "banana"]          # mixed types (allowed!)
nestedList = ["apple", "banana", [1, 2, 3]]     # a list inside a list
emptyList  = []                                 # empty list
```

- `type(myList)` is `<class 'list'>`.
- **Nested indexing:** `nestedList[2]` → `[1, 2, 3]`; `nestedList[2][1]` → `2`.

## 2. Indexing & access — `01_lists.py`, `02_lists.py`

- **Positive index** (0-based, front→back): `a[0]` is first.
- **Negative index** (back→front): `a[-1]` is last, `a[-2]` second-last.
- Accessing an out-of-range index raises `IndexError`.

## 3. Length & membership — `02_lists.py`

- `len(a)` → number of items (**O(1)**).
- `value in a` → `True`/`False` membership test (**O(n)**, scans the list).

## 4. Traversal — `02_lists.py`

| Pattern | Use |
|---------|-----|
| `for x in a:` | iterate over the items directly |
| `for i in range(len(a)):` | iterate by index (`a[i]`) |
| `for i, x in enumerate(a):` | index **and** value together |
| `for i, x in enumerate(a, start=1):` | same, but counting from 1 |
| `for x, y in zip(a, b):` | walk **two** lists in parallel (stops at the shorter; `strict=True` requires equal lengths) |

- **Unpacking:** `a, b, c = [1, 2, 3]` (counts must match), `first, *rest = [...]`
  (star grabs the remainder as a list), and the no-temp swap `x, y = y, x`.

## 5. Adding & updating elements — `03_lists.py`

| Operation | Effect | Cost |
|-----------|--------|------|
| `a[i] = v` | replace the item at index `i` (in place) | O(1) |
| `a.insert(i, v)` | insert `v` *before* index `i` (shifts the rest right) | O(n) |
| `a.append(v)` | add one item to the end | amortized O(1) |
| `a.extend(other)` | add all items of another iterable to the end | O(k) |

> `append(x)` adds **one** element (a list `[1,2]` appended becomes `[..., [1,2]]`).
> `extend([1,2])` adds the elements (`[..., 1, 2]`).

## 6. Slicing — `04_lists.py`

`a[start:stop:step]` — `start` included, `stop` excluded; returns a **new list**.

| Slice | Meaning |
|-------|---------|
| `a[0:3]` | items 0,1,2 |
| `a[3:]` / `a[:3]` | from 3 to end / start to 3 |
| `a[-3:]` | last 3 items |
| `a[::-1]` | a reversed **copy** |
| `a[::2]`, `a[1::2]` | every 2nd item (from 0, from 1) |
| `a[i:j] = [...]` | **slice assignment** — replace a whole range at once |

## 7. Removing elements — `04_lists.py`

| Operation | Removes | Returns? | Cost |
|-----------|---------|----------|------|
| `a.pop()` | the **last** item | yes | O(1) |
| `a.pop(i)` | the item at index `i` | yes | O(n) |
| `a.remove(x)` | the **first** matching value | no | O(n) |
| `del a[i]` / `del a[i:j]` | by index / by slice | no | O(n) |
| `a.clear()` | **all** items (→ `[]`) | no | O(n) |

> `remove`/`pop` delete **one** item. To remove all occurrences, rebuild:
> `a = [x for x in a if x != value]`.

## 8. Searching — `05_lists.py`

- `x in a` — membership, **O(n)**.
- `a.index(x)` — first position of `x`; `a.index(x, start)` searches from an offset.
  ⚠️ raises `ValueError` if `x` is absent.
- `a.count(x)` — how many times `x` appears, **O(n)**.
- **Linear search** — scan each item, **O(n)**; works on any list.
- **Binary search** — **O(log n)**, but **only on a sorted list**:
  `mid = (left + right) // 2`, then move `left`/`right` inward.

## 9. Operators & aggregates — `06_lists.py`

- `a + b` → **concatenation** (new list), **O(n+m)**.
- `a * 3` → **repetition** (new list with contents repeated).
- `len(a)`, `max(a)`, `min(a)`, `sum(a)` → aggregates, **O(n)** (`len` is O(1)).
- Average idiom: `sum(a) / len(a)`.

## 10. Sorting & reversing — `07_lists.py`

| Call | In place? | Returns | Note |
|------|-----------|---------|------|
| `a.sort()` | ✅ yes | `None` | ascending |
| `a.sort(reverse=True)` | ✅ yes | `None` | descending |
| `a.sort(key=len)` | ✅ yes | `None` | custom order (by a key function) |
| `sorted(a)` | ❌ no | a **new** sorted list | original untouched |
| `a.reverse()` | ✅ yes | `None` | reverse in place |
| `reversed(a)` | ❌ no | an **iterator** | wrap in `list(...)` |
| `a[::-1]` | ❌ no | a reversed **copy** | |

> ⚠️ **`sorted(a)` and `reversed(a)` do NOT modify `a`** — they return a new
> result you must capture. `a.sort()`/`a.reverse()` change `a` and return `None`
> (so `a = a.sort()` is a classic bug — it makes `a` become `None`).

## 11. Copying & aliasing — `07_lists.py` ⭐

This is the most important "gotcha" with lists.

```python
b = a            # ALIAS: b and a are the SAME list (b is a -> True)
b.append(9)      # ...so this also changes a!

c = a.copy()     # COPY: independent (c is a -> False, c == a -> True)
c.append(9)      # ...does NOT change a
```

- A plain `=` does **not** copy — it makes another name for the same list.
- Shallow copies: `a.copy()`, `list(a)`, `a[:]`.
- **Shallow vs deep:** a shallow copy duplicates the **outer** list but **shares the
  inner lists**. Use `copy.deepcopy(a)` to copy nested lists all the way down.
- `is` checks **identity** (same object); `==` checks **equality** (same contents).

## 12. Strings ↔ lists — `07_lists.py`

- `list("spam")` → `['s', 'p', 'a', 'm']`.
- `"a-b-c".split("-")` → `['a', 'b', 'c']`.
- `"-".join(['a', 'b', 'c'])` → `"a-b-c"`.

## 13. List comprehensions — `09_lists.py`

A concise way to build a list from an iterable.

```python
[i * 2 for i in nums]                     # transform each item
[ch for ch in "Python"]                   # iterate a string
[i for i in nums if i > 0]                # filter with a condition
[i**2 for i in nums if i < 0]             # transform + filter
[[r*3 + c for c in range(3)] for r in range(3)]   # nested (build 2-D)
[v for row in matrix for v in row]        # nested (flatten: outer loop first)
```

Functional cousins:
- `map(fn, a)` — apply a function to each item (returns an iterator → `list(...)`).
- `filter(fn, a)` — keep items where `fn` is truthy.
- `any(...)` / `all(...)` — boolean aggregates, often with a generator:
  `any(x > 3 for x in a)`, `all(x > 0 for x in a)`.

## 14. Lists as stack & queue — `04_lists.py`

- **Stack (LIFO):** `append()` to push, `pop()` to pop — both **O(1)**.
- **Queue (FIFO):** using a list, `pop(0)` is **O(n)** (shifts every element).
  Use `collections.deque`: `append()` / `popleft()` are both **O(1)**.

## 15. Lists vs NumPy arrays — `08_lists.py`

| | `list` | `numpy.ndarray` |
|--|--------|-----------------|
| Types | mixed allowed | one fixed `dtype` (mixing coerces, e.g. all → strings) |
| `+` | concatenation | element-wise add |
| `*` | repetition | element-wise multiply |
| `- ` `/` `**` with a scalar | **`TypeError`** | element-wise |

> A list does **not** do scalar math: `myList / 2`, `myList + 2`, `myList - 2`,
> `myList ** 2` all raise `TypeError`. `myList * 2` does **not** error — it repeats.

---

## 16. Time complexity

`n` = number of items.

| Operation | Time |
|-----------|------|
| Index access / update `a[i]` | O(1) |
| `len(a)` | O(1) |
| `append(x)` | amortized O(1) |
| `pop()` (end) | O(1) |
| `insert(i, x)` / `pop(i)` / `del a[i]` (middle) | O(n) |
| `remove(x)` | O(n) |
| `x in a`, `index(x)`, `count(x)` | O(n) |
| `min` / `max` / `sum` | O(n) |
| Slice of `k` items | O(k) |
| `a + b` (concatenate) | O(n + m) |
| `copy()` | O(n) |
| `reverse()` | O(n) |
| Linear search | O(n) |
| Binary search (sorted) | O(log n) |
| `sort()` / `sorted()` | O(n log n) |
| List comprehension over `n` | O(n) |

## 17. Space complexity

| Thing | Extra space |
|-------|-------------|
| The list itself | O(n) |
| Index access / membership / linear search | O(1) |
| Binary search (iterative / recursive) | O(1) / O(log n) |
| In-place `reverse` / `sort` | O(1) / O(n) (Timsort temp) |
| Slice / copy / concatenation / comprehension | O(k) / O(n) / O(n+m) / O(n) |
| Stack & queue ops (`append`/`pop`/`popleft`) | O(1) |

---

## Cross-cutting ideas

### Mutability & references
- A list stores **references** to objects. `a[2] = x` repoints that one slot.
- `=` makes an **alias** (same object); `.copy()`/`[:]`/`list()` make an independent
  (shallow) copy; `copy.deepcopy()` copies nested structures fully.

### In-place vs returns-a-new-list
- **In place (return `None`):** `append`, `insert`, `extend`, `remove`, `pop`,
  `sort`, `reverse`, `clear`. Don't write `a = a.sort()`.
- **Returns a new list (original unchanged):** slicing, `a + b`, `a * k`,
  `sorted(a)`, `list(reversed(a))`, comprehensions, `map`/`filter`.
