import array

import numpy as np

# creation of array
my_array = array.array("i")

print("Empty int array:", my_array)

my_array1 = array.array("i", [1, 2, 3, 4, 5])
print("Int array from list:", my_array1)

my_array2 = np.array([1, 2, 3, 4, 5])
print("NumPy array:", my_array2)
my_array3 = np.array([], dtype=int)
print("Empty NumPy array:", my_array3)

# inserting elements in array
my_array1.insert(0, 0)
my_array1.insert(3, 45)
my_array1.insert(100, 88)
print("After inserts (0,3,100):", my_array1)

# array traversal
for i in my_array1:
    print("Item:", i)

# array traversal with index
for i in enumerate(my_array1):
    print("Index, value:", i)

# access array elements
print("Element at index 0:", my_array1[0])
print("Element at index 3:", my_array1[3])
print("Last element:", my_array1[-1])
