# Question: Permutation


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2


list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
print(permutation(list1, list2))
