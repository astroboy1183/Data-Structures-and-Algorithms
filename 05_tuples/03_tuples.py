import sys

# 1. Creating a list vs a tuple (square brackets vs parentheses)
print("\n--- 1. Creating a list and a tuple ---")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print("list:", my_list, type(my_list))
print("tuple:", my_tuple, type(my_tuple))
# Gotcha: a single-element tuple NEEDS a trailing comma.
# (5,) is a tuple, but (5) without a comma is just the integer 5.
single_tuple = (5,)
not_a_tuple = 5
print("(5,) is a tuple:", type(single_tuple))
print("(5) without a comma is an int:", type(not_a_tuple))

# 2. Mutability: a list CAN change, a tuple CANNOT
print("\n--- 2. Mutability ---")
my_list[0] = 99  # allowed: lists are mutable
my_list.append(4)
print("list after change + append:", my_list)
try:
    my_tuple[0] = 99  # not allowed: tuples are immutable
except TypeError as e:
    print("tuple[0] = 99 ->", e)

# 3. Methods: lists have many; tuples have only count() and index()
print("\n--- 3. Available methods ---")
print("tuple.count(1):", my_tuple.count(1))  # tuples support count()
print("tuple.index(2):", my_tuple.index(2))  # ...and index()
try:
    my_tuple.append(4)  # tuples can't grow -> no append()
except AttributeError as e:
    print("tuple.append(4) ->", e)

# 4. Hashability: tuples can be dict keys / set items; lists cannot
print("\n--- 4. Hashability ---")
point_values = {(0, 0): "origin", (1, 2): "p1"}  # tuple keys are fine
print("dict with tuple keys:", point_values)
try:
    bad = {[0, 0]: "origin"}  # lists are unhashable
    print(bad)
except TypeError as e:
    print("dict with list key ->", e)

# 5. Common ground: both support indexing, slicing, len, in, +, *
print("\n--- 5. What they share ---")
sample_list = [10, 20, 30]
sample_tuple = (10, 20, 30)
print("index [0]:", sample_list[0], "|", sample_tuple[0])
print("slice [1:]:", sample_list[1:], "|", sample_tuple[1:])
print("len:", len(sample_list), "|", len(sample_tuple))
print("20 in ...:", 20 in sample_list, "|", 20 in sample_tuple)
print("concatenation:", [1, 2] + [3], "|", (1, 2) + (3,))
print("repetition:", [0] * 3, "|", (0,) * 3)

# 6. Memory: a tuple is lighter than an equivalent list
print("\n--- 6. Memory footprint ---")
print("list size (bytes):", sys.getsizeof([1, 2, 3]))
print("tuple size (bytes):", sys.getsizeof((1, 2, 3)))
