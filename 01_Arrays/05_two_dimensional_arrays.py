# Two Dimensional arrays

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print("Original 2D array:\n", twoDArray)

# axis = 0 means we are adding a new row
# axis = 1 means we are adding a new column

newtwoDArray = np.insert(twoDArray, 2, [1, 2, 3, 4], axis=1)
print("After insert column at index 2:\n", newtwoDArray)

newtwoDArray1 = np.insert(twoDArray, 1, [1, 2, 3, 4], axis=0)
print("After insert row at index 1:\n", newtwoDArray1)

newtwoDArray2 = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print("After append row:\n", newtwoDArray2)

newtwoDArray3 = np.append(twoDArray, [[1], [2], [3], [4]], axis=1)
print("After append column:\n", newtwoDArray3)

# NumPy creation helpers: build arrays without listing every element
print("\n--- NumPy creation helpers ---")
print("zeros(2, 3):\n", np.zeros((2, 3)))
print("ones(5):", np.ones(5))
print("full((2, 2), 7):\n", np.full((2, 2), 7))
print("arange(0, 10, 2):", np.arange(0, 10, 2))
print("linspace(0, 1, 5):", np.linspace(0, 1, 5))
print("eye(3) identity:\n", np.eye(3))

# reshape: rearrange the same data into a new shape, plus key attributes
print("\n--- Reshape and array attributes ---")
reshaped = np.arange(6).reshape(2, 3)
print("arange(6).reshape(2, 3):\n", reshaped)
print("shape:", reshaped.shape, "ndim:", reshaped.ndim)
print("size:", reshaped.size, "dtype:", reshaped.dtype)

# Aggregates along an axis (axis=0 -> down columns, axis=1 -> across rows)
print("\n--- Axis aggregates ---")
print("Sum of all:", twoDArray.sum())
print("Sum down columns (axis=0):", twoDArray.sum(axis=0))
print("Sum across rows (axis=1):", twoDArray.sum(axis=1))
print("Mean of all:", twoDArray.mean())

# Boolean indexing: select the elements that satisfy a condition
print("\n--- Boolean indexing ---")
print("Mask (values > 10):\n", twoDArray > 10)
print("Values > 10:", twoDArray[twoDArray > 10])

# Broadcasting: the operation is applied to every element / row
print("\n--- Broadcasting ---")
print("Every element + 100:\n", twoDArray + 100)
row = [100, 200, 300, 400]
print("Add a row to each row (broadcast):\n", twoDArray + row)
