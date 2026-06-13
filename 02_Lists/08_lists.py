import numpy as np

# Arrays vs Lists
# NOTE: a NumPy array applies arithmetic element-wise, while a Python list does
# NOT support scalar arithmetic. The list lines that would raise a TypeError are
# commented out below (with the exact error) so the file still runs.

# 1. Creating a NumPy array and a Python list, then checking their types
print("\n--- 1. Creating an array and a list; their types ---")
myArray = np.array([1, 2, 3, 4, 5])
myList = [1, 2, 3, 4, 5]
print("Array type:", type(myArray))
print("List type:", type(myList))

# 2. Indexing the element at position 2 (works the same for both)
print("\n--- 2. Indexing [2] ---")
print("Array[2]:", myArray[2])
print("List[2]:", myList[2])

# 3. Multiplication by a scalar (both work, but mean different things)
print("\n--- 3. Multiplication (* 2) ---")
print("Array * 2:", myArray * 2)  # element-wise multiply -> [2 4 6 8 10]
print("List * 2:", myList * 2)  # NOT an error: repeats/concatenates the list

# 4. Division by a scalar
print("\n--- 4. Division (/ 2) ---")
print("Array / 2:", myArray / 2)  # works: element-wise division -> floats
# print(myList / 2)
# ^ ERROR: TypeError: unsupported operand type(s) for /: 'list' and 'int'

# 5. Addition of a scalar
print("\n--- 5. Addition (+ 2) ---")
print("Array + 2:", myArray + 2)  # works: adds 2 to every element
# print(myList + 2)
# ^ ERROR: TypeError: can only concatenate list (not "int") to list

# 6. Subtraction of a scalar
print("\n--- 6. Subtraction (- 2) ---")
print("Array - 2:", myArray - 2)  # works: subtracts 2 from every element
# print(myList - 2)
# ^ ERROR: TypeError: unsupported operand type(s) for -: 'list' and 'int'

# 7. Exponentiation by a scalar
print("\n--- 7. Exponentiation (** 2) ---")
print("Array ** 2:", myArray**2)  # works: squares every element
# print(myList ** 2)
# ^ ERROR: TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

# 8. Mixing types: numbers plus a string (neither line throws an error)
print("\n--- 8. Mixing types (numbers + a string) ---")
myArray = np.array([1, 2, 3, 4, 5, "a"])  # NumPy coerces ALL items to one dtype
myList = [1, 2, 3, 4, 5, "a"]  # a list keeps mixed types as-is
print("Array (numbers coerced to strings):", myArray)
print("List (mixed types kept):", myList)
