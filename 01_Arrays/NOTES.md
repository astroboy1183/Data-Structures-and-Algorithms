# Arrays — Learning Notes

Key takeaways from the code in this folder. Each section maps to the script(s)
where the idea shows up.

---

## 1. Creating arrays — `01_arrays.py`

- Two array tools in Python:
  - **`array.array(typecode, values)`** — standard library, a typed array. `'i'` = signed int.
  - **`numpy.array(values)`** — from NumPy, for numerical work.
- Create empty arrays: `array.array("i")` or `np.array([], dtype=int)`.
- `insert(index, value)` adds at a position. Inserting at an index **beyond the end** (e.g. `insert(100, 88)`) just **appends** — Python clamps the index to the end instead of erroring.

## 2. Traversal & access — `01_arrays.py`

- Plain loop: `for x in my_array`.
- Index + value together: `for i, x in enumerate(my_array)`.
- Indexing: positive (`my_array[0]`) and negative (`my_array[-1]` = last element).

## 3. Searching — `02_arrays.py`

- **Bounds check first:** valid indices are `0 .. len-1`, so the test is `index < len(array)` (not `<=`).
- **Linear search** — scan every element, `O(n)`. Works on any array.
- **Binary search** — `O(log n)`, but **only on a sorted array**. Repeatedly halve the range:
  `mid = (left + right) // 2` (the parentheses matter — `left + right // 2` is a different, wrong value).

## 4. Deletion — `03_arrays.py`

- `remove(value)` — deletes the **first matching value** only (not all occurrences).
- `pop(index)` — deletes and **returns** the element at an index; `pop()` removes the **last** one.
- Neither removes multiple elements. To drop all occurrences, rebuild: `[x for x in arr if x != value]`.

## 5. Array methods reference — `04_arrays_practice.py`

A hands-on tour of the `array.array` methods:

| Method | Purpose |
|--------|---------|
| `append(x)` | add one element to the end |
| `insert(i, x)` | add at index `i` |
| `extend(iterable)` | add many elements |
| `fromlist([...])` | append items from a Python list |
| `remove(x)` / `pop(i)` | delete by value / by index |
| `index(x)` | find the index of a value |
| `reverse()` | reverse in place |
| `count(x)` | how many times `x` appears |
| `buffer_info()` | `(memory address, length)` |
| `tobytes()` / `frombytes(b)` | convert to/from raw bytes |
| `tolist()` | convert to a Python list |
| slicing `a[start:stop:step]` | extract a sub-array |

- **`tobytes`/`frombytes` round-trip:** bytes can be read back into an array of the same typecode. For an `'i'` array the byte count must be a **multiple of 4** (the item size).
- `tostring()` was **removed in Python 3.9** — use `tobytes()`.

## 6. Two-dimensional arrays — `05`, `06`, `07_two_dimensional_arrays.py`

- Built with nested lists: `np.array([[...], [...]])`. Each inner list is a **row**.
- **Axes:** `axis=0` works along **rows**, `axis=1` works along **columns**.
- **Access** an element: `array[row][col]` (or `array[row, col]` in NumPy). Bounds-check with
  `rowIndex < len(array) and colIndex < len(array[0])`.
- **Traverse** with a nested loop (outer = rows, inner = columns).
- **Insert / append / delete** along an axis: `np.insert`, `np.append`, `np.delete` with `axis=`.
  The inserted/appended shape must line up with that axis (e.g. a new column needs one value per row).
- **Columns instead of rows:** transpose with `arr.T`, or build with `np.column_stack([...])`.
- ⚠️ `np.array()` has **no `axis` argument** — `axis` belongs to operations like `insert`, `append`, `delete`, `concatenate`, `sum`.

---

## Cross-cutting ideas

### NumPy resizing always creates a *new* array
An array is a **fixed-size contiguous block of memory**, so it can't grow or shrink in place.
- **NumPy:** `insert`, `append`, `delete` (and `concatenate`, `vstack`/`hstack`) **return a brand-new array** and copy the data (`O(n)`). The original is untouched — you must capture the return value.
- **`list` / `array.array`:** modify **in place** (same object). `append` is amortized `O(1)`; `insert`/`remove` shift elements (`O(n)`).
- ⚠️ Performance trap: calling `np.append` in a loop is `O(n²)`. Build a `list` and convert once with `np.array(list)`, or pre-allocate.
- You **can't truly delete a single cell** from a NumPy array in place (no "holes" allowed) — that's why `np.delete` returns a reshaped copy.

### `list` vs NumPy `ndarray`
| | `list` | NumPy `ndarray` |
|--|--------|-----------------|
| Element types | mixed | one fixed `dtype` |
| Memory | pointers to objects | one compact block |
| Math speed | slow (Python loops) | fast (vectorized C) |
| Size | grows/shrinks in place | fixed; resize = new array |
| `+` operator | concatenation | element-wise add |
| `*` operator | repeat | element-wise multiply |
| Slicing | returns a **copy** | returns a **view** (shares memory) |

- Use a **`list`** for general-purpose, mixed, frequently-resized data.
- Use a **NumPy array** for large numeric data, math, and multi-dimensional structure.

### Complexity quick reference
| Operation | Array |
|-----------|-------|
| Access by index | `O(1)` |
| Linear search | `O(n)` |
| Binary search (sorted) | `O(log n)` |
| Insert / delete (middle) | `O(n)` (shift or copy) |
| Append (list, amortized) | `O(1)` |
