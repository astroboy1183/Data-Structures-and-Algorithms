from collections import deque

# 1. Creating a list
print("\n--- 1. Creating a list ---")
myList = ["a", "b", "c", "d", "e", "f"]
print("Original list:", myList)

# 2. Basic slicing [start:stop] (start is included, stop is excluded)
print("\n--- 2. Basic slicing [start:stop] ---")
print("Slice [0:3]:", myList[0:3])
print("Slice [2:5]:", myList[2:5])

# 3. Open-ended slices: omit start or stop to reach the beginning/end
print("\n--- 3. Open-ended slices [start:] and [:stop] ---")
print("Slice [3:]:", myList[3:])
print("Slice [:3]:", myList[:3])

# 4. Negative-index slice (count from the end)
print("\n--- 4. Negative-index slice [-3:] ---")
print("Slice [-3:]:", myList[-3:])

# 5. Reversing a list with a step of -1
print("\n--- 5. Reversing with [::-1] ---")
print("Reversed [::-1]:", myList[::-1])

# 6. Step slicing [start::step] (take every step-th item)
print("\n--- 6. Step slicing [start::step] ---")
print("Slice [::2]:", myList[::2])
print("Slice [1::2]:", myList[1::2])
print("Slice [::3]:", myList[::3])
print("Slice [1::3]:", myList[1::3])
print("Slice [2::3]:", myList[2::3])
print("Slice [::4]:", myList[::4])
print("Slice [1::4]:", myList[1::4])

# 7. Slice assignment: replace a whole range of elements at once
print("\n--- 7. Slice assignment [start:stop] = [...] ---")
myList[0:2] = ["x", "y"]
print("After slice assignment [0:2]:", myList[:])

# 8. Removing elements with pop() (removes and returns the item)
print("\n--- 8. Removing elements with pop() ---")
myList = ["a", "b", "c", "d", "e", "f"]  # reset to a fresh list
print("Popped last item:", myList.pop())  # no index -> removes the last item
print("After pop():", myList)
myList.pop(1)  # removes the item at index 1
print("After pop(1):", myList)

# 9. Removing elements with the del statement (by index or by slice)
print("\n--- 9. Removing elements with del ---")
del myList[3]
print("After del index 3:", myList)
del myList[0:2]
print("After del [0:2]:", myList)

# 10. Extending the list with another iterable using extend()
print("\n--- 10. Extending the list with extend() ---")
myList.extend(["t", "u", "v"])
print("After extend:", myList)

# 11. Removing the first matching value with remove()
print("\n--- 11. Removing a value with remove() ---")
myList.remove("t")
print("After remove('t'):", myList)

# 12. clear(): remove all elements, leaving an empty list
print("\n--- 12. Emptying a list with clear() ---")
print("Before clear():", myList)
myList.clear()
print("After clear():", myList)

# 13. Using a list as a STACK (LIFO) and a deque as a QUEUE (FIFO)
print("\n--- 13. List as stack, deque as queue ---")
stack = []
stack.append("a")  # push onto the stack
stack.append("b")
stack.append("c")
print("Stack after pushes:", stack)
print("Popped (LIFO):", stack.pop())  # pops "c", the last item pushed
print("Stack now:", stack)

# A list can be a queue too, but pop(0) is O(n) (it shifts every element).
# collections.deque gives O(1) appends/pops at BOTH ends.
queue = deque(["a", "b", "c"])
queue.append("d")  # enqueue at the right end
print("Dequeued (FIFO):", queue.popleft())  # removes "a" from the left in O(1)
print("Queue now:", queue)
