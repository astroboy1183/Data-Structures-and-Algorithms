# 1. Creating a list and checking its type
print("\n--- 1. Creating a list and checking its type ---")
shoppingList = ["Milk", "Cheese", "Butter"]
print("List:", shoppingList)
print("Type:", type(shoppingList))

# 2. Accessing elements by positive index (0-based, front to back)
print("\n--- 2. Accessing elements by positive index ---")
print("Index 0:", shoppingList[0])
print("Index 1:", shoppingList[1])
print("Index 2:", shoppingList[2])

# 3. Accessing elements by negative index (back to front, -1 is the last item)
print("\n--- 3. Accessing elements by negative index ---")
print("Index -1:", shoppingList[-1])
print("Index -2:", shoppingList[-2])
print("Index -3:", shoppingList[-3])

# 4. Length of the list
print("\n--- 4. Length of the list ---")
print("Length:", len(shoppingList))

# 5. Membership test with the "in" operator
print("\n--- 5. Membership test with 'in' ---")
print("'Milk' in list:", "Milk" in shoppingList)
print("'Bread' in list:", "Bread" in shoppingList)

# 6. Traversal: iterate over the items directly
print("\n--- 6. Traversal: iterate over items directly ---")
for i in shoppingList:
    print("Item:", i)

# 7. Traversal: iterate using indexes with range(len(...))
print("\n--- 7. Traversal: using range(len(...)) indexes ---")
for i in range(len(shoppingList)):
    print("Item:", shoppingList[i])

# 8. Traversal: iterate with enumerate (gives (index, value) tuples)
print("\n--- 8. Traversal: using enumerate (index, value) ---")
for i in enumerate(shoppingList):
    print("Pair:", i)

# 9. Traversal: enumerate with a formatted "Item N: value" output
print("\n--- 9. Traversal: enumerate with formatted output ---")
for i in enumerate(shoppingList):
    print("Item ", i[0] + 1, ": ", i[1])

# 10. Modifying elements in place (append "+" to each item)
print("\n--- 10. Modifying elements in place ---")
for i in range(len(shoppingList)):
    shoppingList[i] += "+"
    print("Modified item:", shoppingList[i])

# 11. Looping over an empty list (the body never runs)
print("\n--- 11. Looping over an empty list ---")
empty = []
for _ in empty:
    print("I am empty")

# 12. zip(): iterate over two lists in parallel (stops at the shorter one)
print("\n--- 12. zip() two lists in parallel ---")
names = ["Milk", "Cheese", "Butter"]
prices = [50, 120, 90]
for name, price in zip(names, prices, strict=False):  # strict=True checks equal lengths
    print("Item ->", name, "costs", price)

# 13. enumerate(start=...): index + value, counting from a chosen number
print("\n--- 13. enumerate with a custom start ---")
for index, name in enumerate(names, start=1):
    print("Position", index, "->", name)

# 14. Unpacking a list into separate variables
print("\n--- 14. Unpacking a list ---")
a, b, c = [1, 2, 3]  # one variable per element (the counts must match)
print("a, b, c =", a, b, c)
first, *rest = [10, 20, 30, 40]  # star captures the remaining items as a list
print("first:", first, "| rest:", rest)
x, y = 1, 2
x, y = y, x  # swap without a temporary variable
print("after swap -> x:", x, "y:", y)
