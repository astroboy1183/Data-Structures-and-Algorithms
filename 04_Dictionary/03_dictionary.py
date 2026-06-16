# 1. Create, add a key, traverse, and clear a dictionary
print("\n--- 1. Create, add, traverse, clear ---")
myDict = {"name": "Jayanth", "age": 27, "city": "Mumbai", "country": "India"}
print("Original dict:", myDict)
myDict["address"] = "Malad"  # assigning to a new key adds it
print("After adding 'address':", myDict)
for key in myDict:  # iterating a dict yields its keys
    print(key, "->", myDict[key])
myDict.clear()  # remove everything, leaving an empty dict
print("After clear():", myDict)

# 2. copy(): make an independent (shallow) copy
print("\n--- 2. copy() ---")
myDict = {"name": "Jayanth", "age": 27, "city": "Mumbai", "country": "India"}
print("Original dict:", myDict)
myDict1 = myDict.copy()
print("Copy:", myDict1)

# 3. fromkeys(): build a NEW dict from keys, all sharing one default value
print("\n--- 3. fromkeys() ---")
print("fromkeys('abc'):", myDict.fromkeys("abc"))  # default value is None
print("fromkeys(digits, 'abc'):", myDict.fromkeys("1234567890", "abc"))
print("fromkeys([1..5], 'Jayanth'):", myDict.fromkeys([1, 2, 3, 4, 5], "Jayanth"))

# 4. get(): read a value safely; a missing key returns None (or a given default)
print("\n--- 4. get() ---")
print("get('name') ->", myDict.get("name"))  # key exists -> its value
print("get('name1') ->", myDict.get("name1"))  # missing -> None (no KeyError)
print(
    "get('name1', default) ->", myDict.get("name1", "Not Found")
)  # missing -> default

# 5. items(), keys(), values(): the three view objects
print("\n--- 5. items(), keys(), values() ---")
print("items():", myDict.items())
print("keys():", myDict.keys())
print("values():", myDict.values())

# 6. popitem() and pop(): remove items
print("\n--- 6. popitem() and pop() ---")
myDict.popitem()  # remove and return the LAST inserted key-value pair
print("After popitem():", myDict)
myDict.pop("name")  # remove a specific key by name
print("After pop('name'):", myDict)
myDict.pop("name1", None)  # missing key + default -> no KeyError
print("After pop('name1', None):", myDict)

# 7. setdefault(): return a key's value, inserting it with a default if absent
print("\n--- 7. setdefault() ---")
myDict.setdefault("name")  # 'name' absent -> inserted with value None
print("After setdefault('name'):", myDict)
myDict.setdefault("name1", "Hannah")  # absent -> inserted with 'Hannah'
print("After setdefault('name1', 'Hannah'):", myDict)

# 8. update(): merge another dict in, overwriting any existing keys
print("\n--- 8. update() ---")
myDict.update({"name": "Hannah", "age": 27, "city": "Jamshedpur", "country": "India"})
print("After update():", myDict)

# update() also accepts another dict variable (not just a literal)
myDict = {"name": "Hannah", "age": 27, "city": "Jamshedpur", "country": "India"}
newDict = {"name": "Jayanth", "age": 27, "city": "Mumbai", "country": "India"}
myDict.update(newDict)  # values from newDict overwrite myDict's matching keys
print("After update(newDict):", myDict)

# 9. Merge operators (Python 3.9+): | builds a new dict, |= merges in place
print("\n--- 9. Merge operators | and |= ---")
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}
print("a | b (new dict):", a | b)  # on a key clash the RIGHT side wins -> y = 20
a |= b  # in-place merge, equivalent to a.update(b)
print("a after a |= b:", a)

# 10. Counting frequencies with get(): a very common dictionary pattern
print("\n--- 10. Counting with get() ---")
letters = "mississippi"
counts = {}
for ch in letters:
    counts[ch] = counts.get(ch, 0) + 1  # default 0 for a new letter, then add 1
print("Letter counts:", counts)
