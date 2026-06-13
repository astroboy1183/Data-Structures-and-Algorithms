# Arrays — Learning Notes

Key takeaways from the code in this folder, plus the core theory of arrays.
The two array types used here are Python's standard-library **`array.array`** and
NumPy's **`numpy.ndarray`**; all comparisons below are between those two.
Each section maps to the script(s) where the idea shows up.

---

## 0. What is an array?

- An array stores elements in a **contiguous block of memory**, one cell after another.
- All cells are the **same size**, so the address of element `i` is
  `base_address + i * item_size`. That arithmetic is why **indexing is O(1)** — the
  computer jumps straight to the address without scanning.
- Arrays are **homogeneous** (all elements the same type) and store **raw values inline**,
  which makes them memory-compact.
- **Static array:** size fixed at creation (e.g. `numpy.ndarray`).
- **Dynamic array:** grows automatically by allocating a larger block and copying the
  elements over (e.g. `array.array`). Growth is *amortized* O(1) because it keeps spare capacity.

---

## 1. Creating arrays — `01_arrays.py`

- Two array tools in Python:
  - **`array.array(typecode, values)`** — standard library, a typed 1-D array. `'i'` = signed int.
  - **`numpy.array(values)`** — from NumPy, for n-dimensional numerical work.
- Create empty arrays: `array.array("i")` or `np.array([], dtype=int)`.
- `insert(index, value)` adds at a position. Inserting at an index **beyond the end**
  (e.g. `insert(100, 88)`) just **appends** — Python clamps the index instead of erroring.

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
- Neither removes multiple elements. To drop all occurrences, rebuild a new array from the kept items.

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

- **`tobytes`/`frombytes` round-trip:** bytes can be read back into an array of the same
  typecode. For an `'i'` array the byte count must be a **multiple of 4** (the item size).
- `tostring()` was **removed in Python 3.9** — use `tobytes()`.

## 6. Two-dimensional arrays — `05`, `06`, `07_two_dimensional_arrays.py`

- Built with nested lists: `np.array([[...], [...]])`. Each inner list is a **row**.
- **Axes:** `axis=0` works along **rows**, `axis=1` works along **columns**.
- **Access** an element: `array[row][col]` (or `array[row, col]` in NumPy). Bounds-check with
  `rowIndex < len(array) and colIndex < len(array[0])`.
- **Traverse** with a nested loop (outer = rows, inner = columns) → `O(rows × cols)`.
- **Insert / append / delete** along an axis: `np.insert`, `np.append`, `np.delete` with `axis=`.
  The inserted/appended shape must line up with that axis (a new column needs one value per row).
- **Columns instead of rows:** transpose with `arr.T`, or build with `np.column_stack([...])`.
- ⚠️ `np.array()` has **no `axis` argument** — `axis` belongs to operations like `insert`,
  `append`, `delete`, `concatenate`, `sum`.

---

## 7. `array.array` in depth

A thin, memory-efficient wrapper over a C array. The **typecode is mandatory** and fixes
both the element type and how many bytes each element occupies:

| Code | C type | Python type | Bytes (typical) |
|------|--------|-------------|-----------------|
| `'b'` / `'B'` | signed / unsigned char | int | 1 |
| `'h'` / `'H'` | signed / unsigned short | int | 2 |
| `'i'` / `'I'` | signed / unsigned int | int | 4 |
| `'l'` / `'L'` | signed / unsigned long | int | 4 or 8 |
| `'q'` / `'Q'` | signed / unsigned long long | int | 8 |
| `'f'` | float | float | 4 |
| `'d'` | double | float | 8 |

(There is also `'u'` for unicode characters, but it is **deprecated**. Exact int sizes are
platform-dependent — check with `a.itemsize`.)

- **Type enforcement:** every value must match the typecode, so the array stays homogeneous.
  `array.array('i', [1, 2]).append(1.5)` → `TypeError`; appending `"x"` → `TypeError`.
- **Useful attributes:** `a.typecode` (the code) and `a.itemsize` (bytes per element).
- **When to use:** large amounts of homogeneous numeric data you want stored compactly
  (raw values inline, no per-object overhead) when you don't need NumPy's math. For small or
  mixed-type collections, a plain `list` is simpler.

## 8. `numpy.ndarray` in depth

NumPy's array is the foundation of numerical Python: n-dimensional, typed, and vectorized.

### dtype (the element data type)
- Every ndarray has **one `dtype`** shared by all elements. Common ones: `int8/16/32/64`,
  `uint8…`, `float32/64`, `bool_`, `complex128`, `str_`, `object`.
- **Set it explicitly:** `np.array([1, 2, 3], dtype=np.float64)` or `dtype="int32"`.
- **Inferred** otherwise: `np.array([1, 2, 3])` → `int64`; `np.array([1.0, 2])` → `float64`.
- **Coercion to a common type:** all elements are forced into one dtype. `np.array([1, 2, "a"])`
  makes them **all strings** (`'<U21'`) — which is why slipping a string into a numeric array
  silently turns the numbers into text (seen in `02_Lists/08_lists.py`).

### Key attributes (no parentheses — they're attributes, not methods)
| Attribute | Meaning |
|-----------|---------|
| `a.shape` | tuple of dimensions, e.g. `(3, 4)` |
| `a.ndim` | number of dimensions |
| `a.size` | total number of elements |
| `a.dtype` | element data type |
| `a.itemsize` | bytes per element |
| `a.T` | transpose (rows ↔ columns) |

### Creation helpers (besides `np.array`)
| Call | Result |
|------|--------|
| `np.zeros((2, 3))` | 2×3 array of `0.0` |
| `np.ones(5)` | `[1. 1. 1. 1. 1.]` |
| `np.full((2, 2), 7)` | 2×2 array of `7` |
| `np.arange(0, 10, 2)` | `[0 2 4 6 8]` (like `range`) |
| `np.linspace(0, 1, 5)` | 5 evenly spaced values from 0 to 1 |
| `np.eye(3)` | 3×3 identity matrix |

- **Reshape:** `np.arange(6).reshape(2, 3)` rearranges the same data into a new shape.

### Broadcasting
NumPy "stretches" a smaller shape to match a larger one in element-wise ops, **without copying**:
- Scalar: `arr + 10` adds 10 to every element.
- A `(3,)` row can be added to a `(4, 3)` matrix — it's applied to each row.
- Shapes are compatible when each dimension is **equal or one of them is 1**; otherwise `ValueError`.

### Views vs copies
A slice is a **view** that shares memory — editing it changes the original:
```python
a = np.array([1, 2, 3, 4])
b = a[1:3]
b[0] = 99            # a is now [1, 99, 3, 4]  (shared memory!)
c = a[1:3].copy()    # c is independent; editing c leaves a alone
```

## 9. `array.array` vs `numpy.ndarray`

Both store raw values in a **compact contiguous buffer**. The difference is dimensionality
and computing power.

| Aspect | `array.array` (stdlib) | `numpy.ndarray` (NumPy) |
|--------|------------------------|--------------------------|
| Import | built-in `array` (no install) | `pip install numpy` |
| Purpose | memory-efficient typed **1-D** sequence | **n-dimensional** numerical computing |
| Dimensions | 1-D only | 1-D, 2-D, 3-D, … (`.shape`, `.ndim`) |
| Type system | one typecode (`'i'`, `'f'`, `'d'`, …) | rich `dtype`s (`int8/32/64`, `float64`, `bool`, `complex`, …) |
| Allowed values | numbers / chars only | numbers, bool, strings, even objects |
| Scalar math | none — `* ` repeats, `+` concatenates two arrays; `/`, `-` raise `TypeError` | **element-wise / broadcasting** (`* 2` multiplies each element, etc.) |
| Slicing | returns a **copy** | returns a **view** (shares memory) |
| Resizing | in place: `append` amortized O(1), `insert`/`remove` O(n) | fixed size; resize ops return a **new array** |
| Methods | small, list-like (`append`, `insert`, `pop`, …) | huge math API (`reshape`, `sum(axis)`, `dot`, `mean`, …) |
| Use when | you need compact 1-D numeric storage without a dependency | you need math, vectorization, or multiple dimensions |

> Rule of thumb: **`array.array`** = compact typed 1-D storage.
> **`numpy.ndarray`** = a fast, multi-dimensional math engine.

---

## 10. Time complexity

For a 1-D array (`n` = number of elements). "Dynamic array" here means `array.array`.

| Operation | Time | Why |
|-----------|------|-----|
| Access / update by index `a[i]` | **O(1)** | direct address arithmetic |
| Search — unsorted (linear) | **O(n)** | may scan every element |
| Search — sorted (binary) | **O(log n)** | halves the range each step |
| Membership `x in a` | **O(n)** | linear scan |
| `min` / `max` / `sum` | **O(n)** | visits every element |
| Append at end | **amortized O(1)** | occasional resize-and-copy averages out |
| Insert at start / middle | **O(n)** | must shift later elements right |
| Delete at end (`pop()`) | **O(1)** | nothing to shift |
| Delete at start / middle | **O(n)** | must shift later elements left |
| Slice of `k` elements | **O(k)** | copies those elements |
| Concatenate (`a + b`) | **O(n + m)** | builds a new array |
| Copy / `tolist()` | **O(n)** | copies all elements |
| Reverse | **O(n)** | touches every element |
| Sort | **O(n log n)** | comparison sort |
| 2-D full traversal | **O(rows × cols)** | visits every cell |

> NumPy note: any size-changing op (`np.insert`, `np.append`, `np.delete`,
> `concatenate`) is **O(n)** because it allocates a new array and copies. Doing this in a
> loop is **O(n²)** — instead **pre-allocate** with `np.zeros`/`np.empty` and fill by index.

## 11. Space complexity

| Thing | Extra (auxiliary) space | Note |
|-------|-------------------------|------|
| Storing the array itself | **O(n)** | n cells of fixed-size memory |
| Access / update / linear search | **O(1)** | no extra storage |
| Binary search (iterative) | **O(1)** | just a few index variables |
| Binary search (recursive) | **O(log n)** | call-stack depth |
| In-place reverse | **O(1)** | swaps in place |
| Sort | **O(n)** worst case | needs temporary memory |
| Slice / concatenate / copy | **O(k)** / **O(n + m)** / **O(n)** | result is a new array |
| NumPy slice (view) | **O(1)** | shares the original buffer, no copy |
| Building a new array (`np.insert`/`append`/`delete`) | **O(n)** | new buffer allocated |

---

## Cross-cutting ideas

### Resizing a fixed array creates a *new* array
An array is a **fixed-size contiguous block**, so it can't grow or shrink in place.
- **NumPy:** `insert`, `append`, `delete` (and `concatenate`, `vstack`/`hstack`) **return a
  brand-new array** and copy the data (`O(n)`). The original is untouched — capture the return value.
- **`array.array`:** modifies **in place** (same object). `append` is amortized `O(1)`;
  `insert`/`remove` shift elements (`O(n)`).
- You **can't truly delete a single cell** from a NumPy array in place (no "holes" allowed) —
  that's why `np.delete` returns a reshaped copy.

### In-place vs new object
- Assigning an **element value** (`a[2] = 5`) overwrites the raw value in the buffer — the
  container is the same object, no new array is created (true for both `array.array` and NumPy).
- Changing the **number of elements** is in place for `array.array`, but makes a **new array**
  in NumPy.
