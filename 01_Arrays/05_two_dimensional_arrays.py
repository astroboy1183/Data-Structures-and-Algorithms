# Two Dimensional arrays

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(twoDArray)

# axis = 0 means we are adding a new row
# axis = 1 means we are adding a new column

newtwoDArray = np.insert(twoDArray, 2, [1, 2, 3, 4], axis=1)
print(newtwoDArray)

newtwoDArray1 = np.insert(twoDArray, 1, [1, 2, 3, 4], axis=0)
print(newtwoDArray1)

newtwoDArray2 = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newtwoDArray2)

newtwoDArray3 = np.append(twoDArray, [[1], [2], [3], [4]], axis=1)
print(newtwoDArray3)
