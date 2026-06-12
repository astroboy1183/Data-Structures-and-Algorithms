import array

# 1. Create an array and traverse.

print("# 1. Create an array and traverse.\n")
my_array = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in my_array:
    print(i)
print("__________________________________________________________\n")

# 2. Access individual elements through indexes

print("# 2. Access individual elements through indexes.\n")
print(my_array[0])
print(my_array[1])
print(my_array[-1])
print("__________________________________________________________\n")

# 3. Append any value to the array using append() method

print("# 3. Append any value to the array using append() method.\n")

my_array.append(11)
print(my_array)
print("__________________________________________________________\n")

# 4. Insert value in an array using insert() method

print("# 4. Insert value in an array using insert() method.\n")

my_array.insert(3, 0)
print(my_array)
print("__________________________________________________________\n")

# 5. Extend python array using extend() method

print("# 5. Extend python array using extend() method.\n")

temp_array = array.array("i", [12, 13, 14])
my_array.extend(temp_array)
print(my_array)
print("__________________________________________________________\n")

# 6. Add items from list into array using fromlist() method

print("# 6. Add items from list into array using fromlist() method.\n")

temp_list = [15, 16, 17]
my_array.fromlist(temp_list)
print(my_array)
print("__________________________________________________________\n")

# 7. Remove any array element using remove() method

print("# 7. Remove any array element using remove() method.\n")

my_array.remove(15)
print(my_array)
print("__________________________________________________________\n")

# 8. Remove last array element using pop() method

print("# 8. Remove last array element using pop() method.\n")

my_array.pop()
print(my_array)
print("__________________________________________________________\n")

# 9. Fetch any element through its index using index() method

print("# 9. Fetch any element through its index using index() method.\n")

print(my_array.index(10))
print("__________________________________________________________\n")

# 10. Reverse a python array using reverse() method

print("# 10. Reverse a python array using reverse() method.\n")

my_array.reverse()
print(my_array)
print("__________________________________________________________\n")

# 11. Get array buffer information through buffer_info() method

print("# 11. Get array buffer information through buffer_info() method.\n")

print(my_array.buffer_info())
print("__________________________________________________________\n")

# 12. Check for number of occurrences of an element using count() method

print("# 12. Check for number of occurrences of an element using count() method.\n")

print(my_array.count(1))
print("__________________________________________________________\n")

# 13. Convert array to string using tobytes() method.

print("# 13. Convert array to string using tobytes() method.\n")

bytes_temp = my_array.tobytes()
print(bytes_temp)
ints = array.array("i")
ints.frombytes(bytes_temp)
print(ints)
print("__________________________________________________________\n")

# 14. Convert array to a python list with same elements using tolist() method

print(
    "# 14. Convert array to a python list with same elements using tolist() method.\n"
)

print(my_array.tolist())
print("__________________________________________________________\n")

# 15. Append raw bytes to the array using frombytes() method
# (for an 'i' array the byte count must be a multiple of the item size, 4 bytes)

print("# 15. Append raw bytes to the array using frombytes() method.\n")

my_array.frombytes(b"\x01\x00\x00\x00")  # appends the integer 1
print(my_array)
print("__________________________________________________________\n")

# 16. Slice elements from an array
print("# 16. Slice elements from an array.\n")
print(my_array[0:5])
print(my_array[5:10])
print(my_array[0:10:2])
print(my_array[0:10:3])
print(my_array[0:10:4])
print(my_array[0:10:5])
print(my_array[0:10:6])
print(my_array[0:10:7])
print(my_array[0:10:8])
print(my_array[0:10:9])
print(my_array[0:10:10])
print("__________________________________________________________\n")
