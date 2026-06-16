from random import randint

# 1. Dict comprehension: build a dict by looping over an iterable
print("\n--- 1. Building a dict with a comprehension ---")
city_names = ["Paris", "London", "Rome", "Berlin", "Madrid"]
# {key: value for item in iterable} -> give each city a random temp (20-30)
city_temps = {city: randint(20, 30) for city in city_names}
print("City temps:", city_temps)

# 2. Dict comprehension with a condition (filter while building)
print("\n--- 2. Filtering a dict with a comprehension ---")
# keep only the (city, temp) pairs where temp > 25
new_dict = {city: temp for (city, temp) in city_temps.items() if temp > 25}
print("Cities warmer than 25:", new_dict)


"""
Define a function that takes two dictionaries, merges them, and sums the
values of any common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}

"""


# merge two dictionaries, summing the values of any common keys
def merge_dicts(dict1, dict2):
    new_dict = {}  # start empty (initialising this was the missing piece)
    for key in dict1:
        if key in dict2:
            new_dict[key] = dict1[key] + dict2[key]  # common key -> sum values
        else:
            new_dict[key] = dict1[key]  # only in dict1 -> keep as-is
    for key in dict2:
        if key not in new_dict:
            new_dict[key] = dict2[key]  # only in dict2 -> add it
    return new_dict


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
print("\n--- merge_dicts ---")
print("Merged (common keys summed):", merge_dicts(dict1, dict2))
