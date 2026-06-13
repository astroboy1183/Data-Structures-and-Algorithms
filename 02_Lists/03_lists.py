# 1. Creating a list and checking its type
print("\n--- 1. Creating a list and checking its type ---")
myList = [1, 2, 3, 4, 5, 6, 7]
print("Original list:", myList)
print("Type:", type(myList))

# 2. Updating elements by index (repoints those slots to the new values)
print("\n--- 2. Updating elements by index ---")
myList[2] = 33
myList[3] = 44
print("After updating index 2 and 3:", myList)

# 3. Inserting elements at a given position with insert(index, value)
print("\n--- 3. Inserting elements with insert() ---")
myList.insert(0, 11)
print("After insert(0, 11):", myList)
myList.insert(4, 55)
print("After insert(4, 55):", myList)

# 4. Appending elements to the end with append()
print("\n--- 4. Appending elements with append() ---")
myList.append(77)
print("After append(77):", myList)
myList.append(88)
print("After append(88):", myList)

# 5. Extending the list with another list using extend()
print("\n--- 5. Extending the list with extend() ---")
newList = [213, 423, 2, 534, 234]
myList.extend(newList)
print("After extend(newList):", myList)
