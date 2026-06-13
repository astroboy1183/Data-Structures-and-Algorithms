# traversing a two dimensional array

import numpy as np

twoDArray = np.array(
    ([1, 2, 3, 4], [1, 23, 25, 547], [45, 456, 345, 5785], [789, 345, 6789, 243])
)
print("2D array:\n", twoDArray)


def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print("Element:", array[i][j])


traverseArray(twoDArray)

# searching a two dimensional array


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "Element found at position " + str(i) + ", " + str(j)
    return "Element not found"


print("Search for 789 ->", searchTDArray(twoDArray, 789))
print("Search for 100 ->", searchTDArray(twoDArray, 100))

# deletion of row/column from a two dimensional array

newTDArray = np.delete(twoDArray, 1, axis=1)
print("After deleting column 1:\n", newTDArray)

newTDArray1 = np.delete(twoDArray, 1, axis=0)
print("After deleting row 1:\n", newTDArray1)

# deletion of an element from a two dimensional array


def deleteElement(array, rowIndex, colIndex):
    if rowIndex < len(array) and colIndex < len(array[0]):
        # A fixed-size array can't have a "hole", so a single cell can't truly be
        # removed; we blank it with 0 (None can't be stored in an int array).
        array[rowIndex][colIndex] = 0
        return array
    else:
        return "Index out of bounds"


print("After deleting element [1][2]:\n", deleteElement(twoDArray, 1, 2))
print("After deleting element [3][1]:\n", deleteElement(twoDArray, 3, 1))
