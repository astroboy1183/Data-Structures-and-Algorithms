# 1. Basic list comprehension: transform each element (double it)
print("\n--- 1. Basic list comprehension (double each) ---")
prev_list = [1, 2, 3]
new_list = [i * 2 for i in prev_list]
print("Original list:", prev_list)
print("Doubled values:", new_list)

# 2. Comprehension over a string: iterate its characters
print("\n--- 2. Comprehension over a string ---")
language = "Python"
new_list = [letter for letter in language]
print("Characters:", new_list)

# 3. Comprehension with a condition (filter while building the list)
print("\n--- 3. Comprehension with a condition ---")
prev_list = [1, 23, 23, 4 - 234, 234, -235, -12435, -456457, 2345]
positive_list = [i for i in prev_list if i > 0]  # keep only positives
print("Positive numbers:", positive_list)
negative_list = [i**2 for i in prev_list if i < 0]  # square only the negatives
print("Squares of negatives:", negative_list)

# 4. Comprehension with a helper function: keep only consonants
print("\n--- 4. Comprehension with a helper function ---")
sentence = "My name is Jayanth Appalla."


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]
print("Consonants:", consonants)

# 5. map(): apply a function to every item (a functional cousin of a comprehension)
print("\n--- 5. map() ---")
nums = [1, 2, 3, 4]
squared = list(map(lambda n: n**2, nums))  # map returns an iterator -> wrap in list()
print("Squared with map():", squared)

# 6. filter(): keep only the items for which the function returns True
print("\n--- 6. filter() ---")
evens = list(filter(lambda n: n % 2 == 0, nums))
print("Evens with filter():", evens)

# 7. any() / all(): boolean aggregates over a sequence
print("\n--- 7. any() and all() ---")
print("any number > 3?", any(n > 3 for n in nums))
print("all numbers > 0?", all(n > 0 for n in nums))

# 8. Nested list comprehension: build and flatten a 2-D list
print("\n--- 8. Nested list comprehension ---")
matrix = [[row * 3 + col for col in range(3)] for row in range(3)]
print("Built 3x3 matrix:", matrix)
flat = [value for row in matrix for value in row]  # outer loop first, then inner
print("Flattened:", flat)
