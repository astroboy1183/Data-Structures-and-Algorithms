# traversing a two dimensional array

import numpy as np

twoDArray = np.array(
    ([1, 2, 3, 4], [1, 23, 25, 547], [45, 456, 345, 5785], [789, 345, 6789, 243])
)
print(twoDArray)


def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseArray(twoDArray)

# searching a two dimensional array


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "Element found at position " + str(i) + ", " + str(j)
    return "Element not found"


print(searchTDArray(twoDArray, 789))
print(searchTDArray(twoDArray, 100))

# deletion of row/column from a two dimensional array

newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)

newTDArray1 = np.delete(twoDArray, 1, axis=0)
print(newTDArray1)

# deletion of an element from a two dimensional array


def deleteElement(array, rowIndex, colIndex):
    if rowIndex < len(array) and colIndex < len(array[0]):
        array[rowIndex][colIndex] = None
        return array
    else:
        return "Index out of bounds"


print(deleteElement(twoDArray, 1, 2))
print(deleteElement(twoDArray, 3, 1))
