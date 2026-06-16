myTuple = (1, 2, 3, 4, 5, 6, "a")
myTuple1 = (1, 2, 3, "b", "d")
print(myTuple + myTuple1)
myTuple3 = myTuple * 3 + myTuple1 * 2

print(myTuple3.count(1))
print(myTuple3.index(1))

# find multiple indexes of a value
indices = [i for i, value in enumerate(myTuple3) if value == 1]
print(indices)  # e.g. [0, 2, 4, 6, 8]  -> all 5 positions
