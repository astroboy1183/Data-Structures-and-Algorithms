import array

import numpy as np

# creation of array
my_array = array.array("i")

print(my_array)

my_array1 = array.array("i", [1, 2, 3, 4, 5])
print(my_array1)

my_array2 = np.array([1, 2, 3, 4, 5])
print(my_array2)
my_array3 = np.array([], dtype=int)
print(my_array3)

# inserting elements in array
my_array1.insert(0, 0)
my_array1.insert(3, 45)
my_array1.insert(100, 88)
print(my_array1)

# array traversal
for i in my_array1:
    print(i)

# array traversal with index
for i in enumerate(my_array1):
    print(i)

# access array elements
print(my_array1[0])
print(my_array1[3])
print(my_array1[-1])
