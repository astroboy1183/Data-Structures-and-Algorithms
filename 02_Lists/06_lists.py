# 1. Creating two lists
print("\n--- 1. Creating two lists ---")
a = [1, 2, 3]
b = [4, 5, 6]
print("Lists a and b:", a, b)

# 2. Concatenation: + joins two lists into a new one
print("\n--- 2. Concatenation with + ---")
c = a + b
print("Concatenation (a + b):", c)

# 3. Repetition: * repeats the list's contents
print("\n--- 3. Repetition with * ---")
d = a * 3
print("Repetition (a * 3):", d)

# 4. Built-in aggregate functions (len, max, min, sum, average)
print("\n--- 4. Aggregate functions ---")
print("Length:", len(c))
print("Max:", max(c))
print("Min:", min(c))
print("Sum:", sum(c))
print("Average:", sum(c) / len(c))

# 5. Average of numbers entered by the user (manual total and count)
print("\n--- 5. Average from user input (manual counter) ---")
total = 0
count = 0
while True:
    inp = input("Enter a number:")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1

print("Average: ", total / count)


# 6. Same average, but collecting values in a list and using sum()/len()
print("\n--- 6. Average from user input (using list functions) ---")
myList = []
while True:
    inp = input("Enter a number:")
    if inp == "done":
        break
    value = float(inp)
    myList.append(value)

print("Average using list functions: ", sum(myList) / len(myList))
