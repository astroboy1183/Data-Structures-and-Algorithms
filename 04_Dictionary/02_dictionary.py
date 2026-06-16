# 1. Creating a dictionary and adding a new key-value pair
print("\n--- 1. Creating and adding to a dictionary ---")
myDict = {"name": "Jayanth", "age": 27, "city": "Mumbai", "country": "India"}
print("Original dict:", myDict)
myDict["address"] = "Malad"  # assigning to a new key adds it
print("After adding 'address':", myDict)


# 2. Traversing a dictionary (iterating over it yields the keys)
print("\n--- 2. Traversing a dictionary ---")


def traverseDict(dict):
    for key in dict:
        print(key, "->", dict[key])  # key and its value


traverseDict(myDict)

# 3. Searching for a value in a dictionary
print("\n--- 3. Searching for a value ---")


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Element not found"


print("Search for 'Chennai' ->", searchDict(myDict, "Chennai"))
print("Search for 'Mumbai' ->", searchDict(myDict, "Mumbai"))

# 4. Deleting elements from a dictionary
print("\n--- 4. Deleting elements ---")
myDict.pop("address")  # remove a specific key by name
myDict.pop("add", None)
print("After pop('address'):", myDict)

myDict.popitem()  # remove the last inserted key-value pair
print("After popitem():", myDict)

del myDict["name"]  # remove a key with the del statement
print("After del myDict['name']:", myDict)

myDict.clear()  # remove everything, leaving an empty dict
print("After clear():", myDict)

# 5. Traversing with .items() to get the key and value together
print("\n--- 5. Traversing with items() (key, value) ---")
myDict = {"name": "Jayanth", "age": 27, "city": "Mumbai"}
for key, value in myDict.items():  # unpack each (key, value) pair directly
    print(key, "=", value)

# 6. Nested dictionaries: a dictionary whose values are themselves dictionaries
print("\n--- 6. Nested dictionaries ---")
people = {
    "p1": {"name": "Jayanth", "city": "Mumbai"},
    "p2": {"name": "Hannah", "city": "Jamshedpur"},
}
print("Whole nested dict:", people)
print("p1's city:", people["p1"]["city"])  # chain keys to reach inner values
for pid, info in people.items():  # outer key -> inner dict
    print(pid, "->", info["name"], "from", info["city"])
