# Data Structures and Algorithms

A personal, hands-on collection of data structures and algorithms implemented in
Python. Each top-level folder covers one topic, and the scripts inside build up
from basic creation/traversal to common operations and algorithms. Most folders also
include a `NOTES.md` summarizing the key learning points.

## Topics

| Folder | Topic |
|--------|-------|
| [`01_Arrays/`](01_Arrays/) | Arrays (`array.array` + NumPy, 1-D and 2-D) |
| [`02_Lists/`](02_Lists/) | Python lists |
| [`03_Project_Arrays_Lists/`](03_Project_Arrays_Lists/) | Practice problems & interview questions |
| [`04_Dictionary/`](04_Dictionary/) | Dictionaries |
| [`05_tuples/`](05_tuples/) | Tuples |

## Prerequisites

- **Python 3.10+** (developed on Python 3.12)
- **pip** and **venv** — bundled with Python. On Debian/Ubuntu you may first need
  `sudo apt install python3-venv`.

## Getting started

```bash
# 1. Clone the repository
git clone https://github.com/astroboy1183/Data-Structures-and-Algorithms.git
cd Data-Structures-and-Algorithms

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies (NumPy)
pip install -r requirements.txt

# 4. Run any script
python 01_Arrays/01_arrays.py
```

> **Note:** Only the scripts that use NumPy (the array examples and a couple of the
> project files) need the dependency; pure-Python scripts run on a plain install.
> Installing `requirements.txt` covers everything. To leave the environment later, run
> `deactivate`.

## Folders

### `01_Arrays/` — Arrays

Working with Python's built-in [`array`](https://docs.python.org/3/library/array.html)
module and [NumPy](https://numpy.org/) to learn how one- and two-dimensional arrays
are created, traversed, searched, and modified.

**One-dimensional arrays**

| File | What it does |
|------|--------------|
| `01_arrays.py` | **Creating & accessing arrays** with `array.array` and NumPy: insert, traverse (incl. `enumerate`), positive/negative indexing. |
| `02_arrays.py` | **Searching** — bounds-checked access, **linear search**, and **binary search**. |
| `03_arrays.py` | **Deleting elements** with `remove()` / `pop()`. |
| `04_arrays_practice.py` | **Methods walkthrough** — `append`, `insert`, `extend`, `fromlist`, `remove`, `pop`, `index`, `reverse`, `count`, `tobytes`/`frombytes`, `tolist`, slicing, sorting, aggregates. |

**Two-dimensional arrays** (NumPy)

| File | What it does |
|------|--------------|
| `05_two_dimensional_arrays.py` | **Creation & growing** (`np.insert`/`np.append` by axis), creation helpers, reshape, axis aggregates, boolean indexing, broadcasting. |
| `06_two_dimensional_arrays.py` | **Element access** with bounds checking. |
| `07_two_dimensional_arrays.py` | **Traversal, search & deletion** (`np.delete` rows/columns). |

📓 [`01_Arrays/NOTES.md`](01_Arrays/NOTES.md) — array theory, `array.array` vs `numpy.ndarray`, and time/space complexity.

### `02_Lists/` — Lists

| File | What it does |
|------|--------------|
| `01_lists.py` | Creating lists (int / string / mixed / nested / empty) and types. |
| `02_lists.py` | Indexing, `len`, membership, traversal (loops, `enumerate`, `zip`), unpacking. |
| `03_lists.py` | Updating by index, `insert`, `append`, `extend`. |
| `04_lists.py` | Slicing, slice assignment, `pop`/`del`/`remove`/`clear`, list as **stack & queue** (`deque`). |
| `05_lists.py` | Membership, **linear & binary search**, `index`, `count`. |
| `06_lists.py` | Operators (`+`, `*`), aggregates (`len`/`max`/`min`/`sum`), average from input. |
| `07_lists.py` | `split`/`join`, `sort`/`sorted`/`reverse` (+ `key`), **copy/aliasing**, shallow vs deep copy. |
| `08_lists.py` | **Lists vs NumPy arrays** — operator differences, mixed types. |
| `09_lists.py` | List comprehensions, plus `map`/`filter`/`any`/`all` and nested comprehensions. |

📓 [`02_Lists/NOTES.md`](02_Lists/NOTES.md) — full list reference, complexity, and the copy/aliasing gotchas.

### `03_Project_Arrays_Lists/` — Practice problems & interview questions

| File | What it does |
|------|--------------|
| `01_problem.py` | Average of daily temperatures; count days above average. |
| `02_problem.py` | **Two Sum** — brute force vs the optimal hash-map solution. |
| `03_problem.py` | Linear search for a number in an array. |
| `04_problem.py` | **Permutation check** — are two lists rearrangements of each other? |
| `05_problem.py` | In-place: reverse a list, transpose a matrix, rotate a matrix left/right. |
| `InterviewQuestions.py` | Assorted problems: missing number, two sum, max product, middle, diagonal sum, best score, remove duplicates, pairs, contains-duplicate, permutation, rotate matrix. |

📄 [`list_vs_array_vs_numpy.md`](03_Project_Arrays_Lists/list_vs_array_vs_numpy.md) — a comprehensive `list` vs `array.array` vs `numpy.ndarray` comparison.

### `04_Dictionary/` — Dictionaries

| File | What it does |
|------|--------------|
| `01_dictionary.py` | Creating dicts (many ways, incl. `zip` & `fromkeys`), `keys`/`values`/`items`, hashable keys. |
| `02_dictionary.py` | Add, traverse (keys & items), search, delete (`pop`/`popitem`/`del`/`clear`), **nested dicts**. |
| `03_dictionary.py` | Methods — `copy`, `fromkeys`, `get`, `setdefault`, `update`, merge `|`/`|=`, counting with `get`. |
| `04_dictionary.py` | Membership, `len`, `all`/`any`/`sorted`, equality, **sort by value**, frequency without a dict. |
| `05_dictionary.py` | Dict comprehensions and a merge-and-sum function. |

📓 [`04_Dictionary/NOTES.md`](04_Dictionary/NOTES.md) — full dictionary reference, common patterns, complexity, and gotchas.

### `05_tuples/` — Tuples

| File | What it does |
|------|--------------|
| `01_tuples.py` | Creating tuples (literal, single-element, from string/list), indexing, slicing, traversal, search. |
| `02_tuples.py` | Concatenation/repetition, `count`/`index`, finding **all** indices of a value. |
| `03_tuples.py` | **List vs tuple** — mutability, methods, hashability, memory footprint. |

📓 [`05_tuples/NOTES.md`](05_tuples/NOTES.md) — tuple reference, list-vs-tuple, immutability nuances, and complexity.

## Code style

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting;
the rules live in [`ruff.toml`](ruff.toml). Install it with `pip install ruff`, then:

```bash
ruff check .     # lint
ruff format .    # auto-format
```

## Conventions

- Folders are numbered (`01_`, `02_`, …) to suggest a learning order.
- Files within a folder are likewise numbered and progress from simple to more involved.
- Console output is printed in labeled blocks (`--- N. ... ---`) so it's easy to follow.
