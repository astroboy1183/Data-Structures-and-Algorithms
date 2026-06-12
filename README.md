# Data Structures and Algorithms

A personal, hands-on collection of data structures and algorithms implemented in
Python. Each top-level folder covers one topic, and the scripts inside build up
from basic creation/traversal to common operations and algorithms.

## Getting started

```bash
# Activate the virtual environment (created with: python3 -m venv .venv)
source .venv/bin/activate

# Run any script
python 01_Arrays/01_arrays.py
```

> Note: `01_Arrays/01_arrays.py` uses NumPy. If it isn't installed, run
> `pip install numpy` inside the activated environment.

## Folders

### `01_Arrays/` — Arrays

Working with Python's built-in [`array`](https://docs.python.org/3/library/array.html)
module (and a little NumPy) to learn how arrays are created, traversed, searched,
and modified.

| File | What it does |
|------|--------------|
| `01_arrays.py` | **Creating & accessing arrays.** Creates arrays with `array.array` and NumPy, inserts elements at given positions, traverses with and without indices (`enumerate`), and accesses elements by positive/negative index. |
| `02_arrays.py` | **Searching.** Implements an `accessElement` helper plus **linear search** and **binary search** functions, with example calls. |
| `03_arrays.py` | **Deleting elements.** Demonstrates removing a value with `remove()` (and shows `pop()` usage in commented-out lines). |
| `04_arrays.py` | **Array operations cheat sheet.** A numbered walkthrough of the common `array` methods: `append`, `insert`, `extend`, `fromlist`, `remove`, `pop`, `index`, `reverse`, `buffer_info`, `count`, `tolist`, and slicing. |

## Conventions

- Folders are numbered (`01_`, `02_`, …) to suggest a learning order.
- Files within a folder are likewise numbered and progress from simple to more involved.
