# Read daily high temperatures and report how many days were above average.

n = int(input("How many Day's Temperature?"))
temps = []

for i in range(0, n):
    temp_input = float(input("Day " + str(i + 1) + "'s high temp:"))
    temps.append(temp_input)

if n == 0:  # avoid dividing by zero
    print("No temperatures entered.")
else:
    mean = sum(temps) / n  # exact mean for comparison; round only for display
    average = round(mean, 2)
    print(average)

    count = 0
    for j in temps:
        if j > mean:
            count += 1

    print(str(count) + " day(s) above average")
