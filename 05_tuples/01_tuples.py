newTuple = (1, 2, 3, 4)
print(newTuple)

newTuple1 = (2,)
print(newTuple1)

newTuple2 = tuple("abcdef")
print(newTuple2)

newTuple3 = tuple([1, 2, 3, 4])
print(newTuple3)

print(newTuple[1])

newTuple4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(newTuple4[3:6])
print(newTuple4[:3:-2])
print(newTuple4[:-1:-3])
print(newTuple4[:-1])

for i in range(len(newTuple4)):
    print(newTuple4[i])

for i in newTuple4:
    print(i)

# search for a value

print(4 in newTuple4)
print(4 not in newTuple4)

print(newTuple4.index(10))
print(newTuple4.count(13))


def searchTuple(tup, element):
    for i in range(len(tup)):
        if tup[i] == element:
            return i
    return -1


print(searchTuple(newTuple4, 10))
