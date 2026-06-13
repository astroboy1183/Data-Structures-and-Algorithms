# `list` vs `array.array` vs `numpy.ndarray`

A comprehensive comparison of Python's three "sequence of items" containers, so you
can pick the right one and avoid the common traps. They look similar but are built
for very different jobs.

## TL;DR — one line each

| Type | One-liner |
|------|-----------|
| **`list`** | Built-in, flexible, holds **anything**; the default general-purpose container. |
| **`array.array`** | Standard-library **compact 1-D** array of one numeric type; like a memory-efficient list of numbers. |
| **`numpy.ndarray`** | Third-party **n-dimensional**, typed, **vectorized** array; the engine of numerical Python. |

```python
my_list  = [1, 2, 3]                      # built-in, no import
import array; my_arr = array.array("i", [1, 2, 3])   # stdlib
import numpy as np; my_nd = np.array([1, 2, 3])       # pip install numpy
```

---

## The big comparison table

| Aspect | `list` | `array.array` | `numpy.ndarray` |
|--------|--------|---------------|-----------------|
| **Import** | built-in | `import array` (stdlib) | `pip install numpy` |
| **Main purpose** | general-purpose collection | compact 1-D numeric storage | numerical / scientific computing |
| **Dimensions** | 1-D (nest lists for more) | **1-D only** | **n-D** (`.shape`, `.ndim`) |
| **Element types** | **mixed / any** | one **typecode** (`'i'`,`'f'`,`'d'`…) | one **dtype** (`int64`, `float64`, `bool`…) |
| **Stores** | **references** to objects | **raw values inline** | **raw values inline** |
| **Memory use** | highest (pointer + object each) | compact | compact |
| **Resizing** | dynamic, **in place** (`append` ~O(1)) | dynamic, **in place** | **fixed** — resize returns a **new** array |
| **`+` operator** | concatenate | concatenate (same typecode) | **element-wise add** |
| **`*` int** | repeat | repeat | **element-wise multiply** |
| **scalar `-` `/` `**`** | `TypeError` | `TypeError` | **element-wise** |
| **Vectorized math** | ❌ | ❌ | ✅ (fast, in C) |
| **Slicing returns** | a **copy** | a **copy** | a **view** (shares memory!) |
| **Type safety** | none (mix freely) | enforced (`TypeError` on wrong type) | coerces all to one dtype |
| **Methods** | rich (`append`, `sort`, `pop`…) | list-like subset | huge math API (`sum(axis)`, `dot`, `reshape`…) |

---

## Operator behaviour (the #1 source of confusion)

```python
[1, 2, 3] + [4]      # list   -> [1, 2, 3, 4]      (concatenate)
arr_i + arr_j        # array  -> concatenation (must share typecode)
np.array([1,2,3]) + np.array([4,5,6])   # numpy -> [5 7 9]   (element-wise)

[1, 2, 3] * 2        # list   -> [1, 2, 3, 1, 2, 3]   (repeat)
np.array([1,2,3]) * 2                    # numpy -> [2 4 6]   (element-wise)
```

| Expression | `list` | `array.array` | `numpy.ndarray` |
|------------|--------|---------------|-----------------|
| `x + 2` | `TypeError` | `TypeError` | adds 2 to each |
| `x - 2` | `TypeError` | `TypeError` | subtracts 2 from each |
| `x * 2` | repeats | repeats | multiplies each |
| `x / 2` | `TypeError` | `TypeError` | divides each |
| `x ** 2` | `TypeError` | `TypeError` | squares each |

> Only **NumPy** does scalar/element-wise arithmetic. `list` and `array.array`
> treat `+`/`*` as sequence concatenation/repetition and reject `-`/`/`/`**`.

---

## Memory model — why this matters

```
list:           NumPy / array.array:
[ ref ] -> 1    [ 1 | 2 | 3 | 4 ]   <- raw values packed together
[ ref ] -> 2     (contiguous, fixed-size cells)
[ ref ] -> 3
[ ref ] -> 4    (objects scattered in memory)
```

- A **`list`** is an array of *pointers* to Python objects → flexible (mixed types)
  but more memory and slower for math (each op goes through a Python object).
- **`array.array`** and **`numpy.ndarray`** store the values *inline* in one block →
  compact and cache-friendly, but every element must be the same type.

---

## Mutability & resizing

- All three let you **change an element**: `x[2] = 9`.
- **`list` / `array.array`** can grow/shrink **in place** (`append` is amortized O(1);
  `insert`/`remove` are O(n) due to shifting).
- **`numpy.ndarray` is fixed-size**: `np.append`, `np.insert`, `np.delete` each build
  and return a **new** array (O(n)). Calling them in a loop is O(n²) — pre-allocate
  with `np.zeros`/`np.empty` instead.

---

## Converting between them

```python
import array, numpy as np

lst = [1, 2, 3]

arr = array.array("i", lst)     # list      -> array.array
nd  = np.array(lst)             # list      -> ndarray

lst2 = arr.tolist()             # array.array -> list
lst3 = nd.tolist()              # ndarray     -> list

nd_from_arr  = np.array(arr)               # array.array -> ndarray
arr_from_nd  = array.array("i", nd)        # ndarray     -> array.array
```

---

## When to use which

- **`list`** — the default. Reach for it unless you have a specific reason not to:
  mixed types, frequent insertion/removal, small-to-medium general data.
- **`array.array`** — you have a **large amount of one numeric type** in 1-D, want it
  stored **compactly**, and **don't** want a NumPy dependency or vectorized math
  (e.g. raw byte/sample buffers).
- **`numpy.ndarray`** — **numeric computation**: vectorized math, linear algebra,
  multi-dimensional data, large datasets, data science / ML.

A common real-world combo: build data up in a **`list`**, then convert once to a
**NumPy array** (`np.array(my_list)`) for the math.

---

## Gotchas cheat-sheet

- **`list` aliasing:** `b = a` does **not** copy — `b` is the same list. Use
  `a.copy()` / `a[:]` (shallow) or `copy.deepcopy(a)` (nested).
- **NumPy slices are views:** `b = a[1:3]; b[0] = 99` also changes `a`. Use
  `a[1:3].copy()` for independence. (`list`/`array.array` slices are copies.)
- **NumPy coerces mixed types:** `np.array([1, 2, "a"])` makes them **all strings**.
  A `list` keeps `[1, 2, "a"]` as-is.
- **`array.array` enforces its typecode:** appending a wrong-type value raises `TypeError`.
- **`* 2` repeats** for `list`/`array.array` (not element-wise) — surprising if you
  expect NumPy behaviour.
- **In-place methods return `None`:** `a = a.sort()` makes `a` become `None`. Use
  `a.sort()` (mutates) or `sorted(a)` (returns a new list).

---

## Complexity quick reference (`n` = number of elements)

| Operation | `list` / `array.array` | `numpy.ndarray` |
|-----------|------------------------|-----------------|
| Index access / update | O(1) | O(1) |
| Append at end | amortized O(1) | O(n) (new array) |
| Insert / delete in middle | O(n) | O(n) (new array) |
| Search (unsorted) | O(n) | O(n) |
| Element-wise math over all | O(n), slow (Python loop) | O(n), fast (vectorized C) |
| Slice of `k` items | O(k) (copy) | O(1) (view) |
