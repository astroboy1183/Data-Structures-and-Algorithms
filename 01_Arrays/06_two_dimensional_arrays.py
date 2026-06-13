import numpy as np

twoDArray = np.array(
    ([1, 2, 3, 4], [1, 23, 25, 547], [45, 456, 345, 5785], [789, 345, 6789, 243])
)
print("2D array:\n", twoDArray)


def accessElement(array, rowIndex, colIndex):
    if rowIndex < len(array) and colIndex < len(array[0]):
        return array[rowIndex][colIndex]
    else:
        return "Index out of bounds"


ans = accessElement(twoDArray, 1, 2)
print("Element at [1][2]:", ans)

ans1 = accessElement(twoDArray, 3, 1)
print("Element at [3][1]:", ans1)
