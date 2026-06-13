import copy

# 1. Converting a string into a list of characters with list()
print("\n--- 1. String to list with list() ---")
a = "spam"
b = list(a)
print("String as list:", b)

# 2. Splitting a string into a list, then joining it back together
print("\n--- 2. split() and join() ---")
c = "spam-spam1-spam2"
delimiter = "-"
d = c.split(delimiter)
print("c after split:", d)
print("after join:", delimiter.join(d))

# 3. Copying, sorting and reversing a list
print("\n--- 3. copy, sort, sorted, reverse ---")
myList = [23, 45, 46, 5, 76, 789, 5, 7, 99]
print("Original list:", myList)
orig = myList.copy()  # copy() makes an independent copy
print("Copy of original list:", orig)
myList.sort()  # sort() sorts in place (ascending)
print("After sort (ascending):", myList)
myList.sort(reverse=True)  # sort() in place, descending
print("After sort (descending):", myList)
sorted(myList)  # sorted() returns a NEW list; result unused -> myList unchanged
print("After sorted() (result unused, list unchanged):", myList)
myList.reverse()  # reverse() reverses in place
print("After reverse:", myList)

# 4. Adding items: append() mutates the list, + builds a new one
print("\n--- 4. append() vs + ---")
myList.append(123)  # append() adds in place
print("After append(123):", myList)
myList + [10]  # + builds a NEW list; result unused -> myList unchanged
print("After + [10] (result unused, list unchanged):", myList)

# 5. Aliasing vs copying: plain assignment shares the SAME object
print("\n--- 5. Aliasing vs copying ---")
original = [1, 2, 3]
alias = original  # NOT a copy: both names point to the same list
alias.append(99)
print("Mutating the alias also changed the original:", original)
independent = original.copy()  # a real (shallow) copy; list(x) / x[:] also work
independent.append(0)
print("Mutating the copy left the original alone:", original)

# 6. Shallow vs deep copy with nested lists
print("\n--- 6. Shallow vs deep copy ---")
nested = [[1, 2], [3, 4]]
shallow = nested.copy()  # copies the OUTER list but SHARES the inner lists
shallow[0].append(99)
print("Shallow copy shares inner lists -> original changed:", nested)
deep = copy.deepcopy(nested)  # copies all the way down
deep[0].append(7)
print("Deep copy is independent -> original unchanged:", nested)

# 7. sort(key=...): sort by a custom rule instead of natural order
print("\n--- 7. Sorting with a key ---")
words = ["banana", "kiwi", "apple", "fig"]
words.sort(key=len)  # sort in place by word length
print("Sorted by length:", words)
print("By length (desc, new list):", sorted(words, key=len, reverse=True))

# 8. reversed(): returns an iterator (wrap in list() to see it)
print("\n--- 8. reversed() vs reverse() vs [::-1] ---")
nums = [1, 2, 3, 4]
print("reversed() -> list:", list(reversed(nums)))  # new order via an iterator
print("Original unchanged by reversed():", nums)  # reversed() does not mutate
