import array

# 1. Create an array and traverse.

print("# 1. Create an array and traverse.\n")
my_array = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in my_array:
    print("Element:", i)
print("__________________________________________________________\n")

# 2. Access individual elements through indexes

print("# 2. Access individual elements through indexes.\n")
print("Element at [0]:", my_array[0])
print("Element at [1]:", my_array[1])
print("Element at [-1]:", my_array[-1])
print("__________________________________________________________\n")

# 3. Append any value to the array using append() method

print("# 3. Append any value to the array using append() method.\n")

my_array.append(11)
print("Array after append:", my_array)
print("__________________________________________________________\n")

# 4. Insert value in an array using insert() method

print("# 4. Insert value in an array using insert() method.\n")

my_array.insert(3, 0)
print("Array after insert:", my_array)
print("__________________________________________________________\n")

# 5. Extend python array using extend() method

print("# 5. Extend python array using extend() method.\n")

temp_array = array.array("i", [12, 13, 14])
my_array.extend(temp_array)
print("Array after extend:", my_array)
print("__________________________________________________________\n")

# 6. Add items from list into array using fromlist() method

print("# 6. Add items from list into array using fromlist() method.\n")

temp_list = [15, 16, 17]
my_array.fromlist(temp_list)
print("Array after fromlist:", my_array)
print("__________________________________________________________\n")

# 7. Remove any array element using remove() method

print("# 7. Remove any array element using remove() method.\n")

my_array.remove(15)
print("Array after remove(15):", my_array)
print("__________________________________________________________\n")

# 8. Remove last array element using pop() method

print("# 8. Remove last array element using pop() method.\n")

my_array.pop()
print("Array after pop:", my_array)
print("__________________________________________________________\n")

# 9. Fetch any element through its index using index() method

print("# 9. Fetch any element through its index using index() method.\n")

print("Index of 10:", my_array.index(10))
print("__________________________________________________________\n")

# 10. Reverse a python array using reverse() method

print("# 10. Reverse a python array using reverse() method.\n")

my_array.reverse()
print("Array after reverse:", my_array)
print("__________________________________________________________\n")

# 11. Get array buffer information through buffer_info() method

print("# 11. Get array buffer information through buffer_info() method.\n")

print("Buffer info:", my_array.buffer_info())
print("__________________________________________________________\n")

# 12. Check for number of occurrences of an element using count() method

print("# 12. Check for number of occurrences of an element using count() method.\n")

print("Count of 1:", my_array.count(1))
print("__________________________________________________________\n")

# 13. Convert array to string using tobytes() method.

print("# 13. Convert array to string using tobytes() method.\n")

bytes_temp = my_array.tobytes()
print("Array as bytes:", bytes_temp)
ints = array.array("i")
ints.frombytes(bytes_temp)
print("Array rebuilt from bytes:", ints)
print("__________________________________________________________\n")

# 14. Convert array to a python list with same elements using tolist() method

print(
    "# 14. Convert array to a python list with same elements using tolist() method.\n"
)

print("Array as list:", my_array.tolist())
print("__________________________________________________________\n")

# 15. Append raw bytes to the array using frombytes() method
# (for an 'i' array the byte count must be a multiple of the item size, 4 bytes)

print("# 15. Append raw bytes to the array using frombytes() method.\n")

my_array.frombytes(b"\x01\x00\x00\x00")  # appends the integer 1
print("Array after frombytes:", my_array)
print("__________________________________________________________\n")

# 16. Slice elements from an array
print("# 16. Slice elements from an array.\n")
print("Slice [0:5]:", my_array[0:5])
print("Slice [5:10]:", my_array[5:10])
print("Slice [0:10:2]:", my_array[0:10:2])
print("Slice [0:10:3]:", my_array[0:10:3])
print("Slice [0:10:4]:", my_array[0:10:4])
print("Slice [0:10:5]:", my_array[0:10:5])
print("Slice [0:10:6]:", my_array[0:10:6])
print("Slice [0:10:7]:", my_array[0:10:7])
print("Slice [0:10:8]:", my_array[0:10:8])
print("Slice [0:10:9]:", my_array[0:10:9])
print("Slice [0:10:10]:", my_array[0:10:10])
print("__________________________________________________________\n")

# 17. Sorting an array.array (there is no .sort() method)
print("# 17. Sorting an array.array (no .sort() method).\n")
sorted_list = sorted(my_array)  # sorted() returns a LIST, not an array
print("sorted() result (a list):", sorted_list)
sorted_array = array.array("i", sorted_list)  # rebuild an array from the list
print("Rebuilt sorted array:", sorted_array)
print("__________________________________________________________\n")

# 18. Aggregate functions work on an array.array
print("# 18. Aggregate functions (min, max, sum, len).\n")
print("Min:", min(my_array))
print("Max:", max(my_array))
print("Sum:", sum(my_array))
print("Length:", len(my_array))
print("__________________________________________________________\n")
