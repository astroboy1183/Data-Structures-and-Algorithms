# 1. Creating an empty dictionary (two equivalent ways)
print("\n--- 1. Creating an empty dictionary ---")
my_dict = dict()  # using the dict() constructor
print("Empty dict via dict():", my_dict)

my_dict2 = {}  # using empty curly braces
print("Empty dict via {}:", my_dict2)

# 2. Creating a dictionary with dict(key=value) keyword arguments
print("\n--- 2. Creating with dict(key=value) ---")
my_dict3 = dict(key1="value1", key2="value2")
print("From keyword args:", my_dict3)

# 3. Creating a dictionary with a {key: value} literal
print("\n--- 3. Creating with a {key: value} literal ---")
my_dict4 = {"key1": "value1", "key2": "value2"}
print("From literal:", my_dict4)

# 4. Creating a dictionary from a list of (key, value) tuples
print("\n--- 4. Creating from a list of tuples ---")
myList = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
my_dict5 = dict(myList)
print("From list of tuples:", my_dict5)

# 5. Viewing a dictionary's keys, values, and items
print("\n--- 5. keys(), values(), items() ---")
my_dict6 = {"key1": "value1", "key2": "value2"}
n = list(my_dict6.items())  # items() -> list of (key, value) tuples
print("items() as a list:", n)
print("Keys:", my_dict6.keys())
print("Values:", my_dict6.values())
print("Items:", my_dict6.items())
print("Type of items():", type(my_dict6.items()))

# 6. Creating a dictionary from two lists with zip()
print("\n--- 6. Creating from two lists with zip() ---")
keys = ["name", "age", "city"]
values = ["Jayanth", 27, "Mumbai"]
my_dict7 = dict(zip(keys, values, strict=True))  # pair each key with a value
print("From zip():", my_dict7)

# 7. Keys must be hashable (immutable): str, int, tuple work - a list does NOT
print("\n--- 7. Keys must be hashable ---")
valid = {("x", "y"): "a tuple key is fine"}  # tuples are hashable -> OK
print("Tuple-key dict:", valid)
# invalid = {["x", "y"]: "value"}
# ^ ERROR: TypeError: unhashable type: 'list' (lists can't be dictionary keys)
