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

> **NumPy required for some scripts.** The NumPy and all two-dimensional examples
> need NumPy. Install it with `pip install numpy` inside the activated environment,
> or system-wide with `sudo apt install python3-numpy`.

## Folders

### `01_Arrays/` — Arrays

Working with Python's built-in [`array`](https://docs.python.org/3/library/array.html)
module and [NumPy](https://numpy.org/) to learn how one- and two-dimensional arrays
are created, traversed, searched, and modified.

**One-dimensional arrays**

| File | What it does |
|------|--------------|
| `01_arrays.py` | **Creating & accessing arrays.** Creates arrays with `array.array` and NumPy, inserts elements at given positions, traverses with and without indices (`enumerate`), and accesses elements by positive/negative index. |
| `02_arrays.py` | **Searching.** Implements an `accessElement` helper plus **linear search** and **binary search** functions, with example calls. |
| `03_arrays.py` | **Deleting elements.** Demonstrates removing a value with `remove()` (and shows `pop()` usage in commented-out lines). |
| `04_arrays_practice.py` | **Array operations walkthrough.** A numbered tour of the common `array` methods: `append`, `insert`, `extend`, `fromlist`, `remove`, `pop`, `index`, `reverse`, `buffer_info`, `count`, `tobytes`/`frombytes`, `tolist`, and slicing. |

**Two-dimensional arrays** (NumPy)

| File | What it does |
|------|--------------|
| `05_two_dimensional_arrays.py` | **Creation & growing.** Builds a 2D array and inserts/appends rows and columns with `np.insert`/`np.append` using `axis=0` (rows) and `axis=1` (columns). |
| `06_two_dimensional_arrays.py` | **Element access.** An `accessElement(array, row, col)` helper with bounds checking. |
| `07_two_dimensional_arrays.py` | **Traversal, search & deletion.** Nested-loop traversal, a search that returns the `(row, col)` position, and row/column deletion with `np.delete`. |

📓 See [`01_Arrays/NOTES.md`](01_Arrays/NOTES.md) for a summary of the key learning
points (search/insert/delete complexity, `list` vs NumPy, and common gotchas).

## Code style

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting;
the rules live in [`ruff.toml`](ruff.toml). To check or format the code:

```bash
ruff check .     # lint
ruff format .    # auto-format
```

## Conventions

- Folders are numbered (`01_`, `02_`, …) to suggest a learning order.
- Files within a folder are likewise numbered and progress from simple to more involved.
