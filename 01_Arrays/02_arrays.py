import array

my_array = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def accessElement(array, index):
    if index < len(array):
        return array[index]
    else:
        return "Index out of bounds"


# linear search
def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return "Element not found"


# binary search
def binarySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Element not found"


print(accessElement(my_array, 2))
print(accessElement(my_array, 10))
print(linearSearch(my_array, 3))
print(linearSearch(my_array, 8))
print(binarySearch(my_array, 3))
print(binarySearch(my_array, 7))
