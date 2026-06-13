# Deleting element from array
import array

my_array = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original array:", my_array)

my_array.remove(3)
print("After remove(3):", my_array)

# my_array.pop(2)
# print(my_array)
# my_array.pop()
# print(my_array)
