# 1. Creating the list and the search target
print("\n--- 1. Creating the list and target ---")
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 50
print("List:", my_list)

# 2. Membership test with the "in" operator
print("\n--- 2. Membership test with 'in' ---")
if target in my_list:
    print("Element found")
else:
    print("Element not found")

# 3. Linear search: scan each element until the target is found (O(n))
print("\n--- 3. Linear search ---")


def linearSearch(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return "Element not found"


print("Linear search for 77 (index or message):", linearSearch(my_list, 77))

# 4. Binary search: repeatedly halve a sorted list (O(log n))
print("\n--- 4. Binary search ---")


def binarySearch(p_list, p_target):
    left, right = 0, len(p_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if p_list[mid] == p_target:
            return mid
        elif p_list[mid] < p_target:
            left = mid + 1
        else:
            right = mid - 1
    return "Element not found"


print("Binary search for 77 (index or message):", binarySearch(my_list, 77))

# 5. index(): the built-in way to find the first position of a value
print("\n--- 5. Finding a position with index() ---")
print("Index of 50:", my_list.index(50))  # raises ValueError if not present
print("Index of 80 (searching from index 3):", my_list.index(80, 3))

# 6. count(): how many times a value appears
print("\n--- 6. Counting occurrences with count() ---")
repeats = [5, 3, 5, 7, 5, 3]
print("List:", repeats)
print("Count of 5:", repeats.count(5))
print("Count of 9:", repeats.count(9))
