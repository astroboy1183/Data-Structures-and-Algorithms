# 1. Membership tests and length
print("\n--- 1. Membership and length ---")
my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
print("'three' not in values:", "three" not in my_dict.values())
print("'three' in values:", "three" in my_dict.values())
print("1 in keys:", 1 in my_dict)  # 'in' on a dict checks the KEYS
print("Length:", len(my_dict))

# 2. all() / any() / sorted() operate on a dict's KEYS
print("\n--- 2. all(), any(), sorted() on keys ---")
my_dict1 = {1: "zero", False: "False"}  # keys are 1 (truthy) and False (falsy)
print("all(keys):", all(my_dict1))  # False -> the key False is falsy
print("any(keys):", any(my_dict1))  # True  -> the key 1 is truthy
print("sorted(keys):", sorted(my_dict1))  # -> [False, 1] (False sorts as 0)

# 3. Comparing dictionaries for equality
print("\n--- 3. Dictionary equality (==) ---")
my_dict3 = {1: "zero", False: "False"}
print("my_dict1 == my_dict3:", my_dict1 == my_dict3)  # True: same keys and values
my_dict3[3] = "three"  # add a new key to my_dict3 only
print("my_dict1:", my_dict1)
print("my_dict3:", my_dict3)
print("my_dict1 == my_dict3:", my_dict1 == my_dict3)  # False: contents now differ

# 4. Sorting a dict by its VALUES (sorted(dict) alone only sorts the keys)
print("\n--- 4. Sorting by value ---")
scores = {"Ana": 88, "Ravi": 72, "Mia": 95, "Leo": 60}
# sort the (key, value) pairs using the value (index 1) as the sort key
print("Items sorted by value:", sorted(scores.items(), key=lambda kv: kv[1]))
# rebuild a dict ordered high -> low (dicts keep insertion order)
ranked = dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))
print("Ranked high to low:", ranked)


# 5. Find the frequency of values in a list WITHOUT using a dictionary
print("\n--- 5. Frequency without a dictionary ---")
nums = [1, 2, 2, 3, 3, 3, 4]
# set() gives each unique value once; list.count() counts its occurrences
frequencies = [(value, nums.count(value)) for value in set(nums)]
print("List:", nums)
print("Frequencies (value, count):", frequencies)
