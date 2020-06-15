friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")



# Use for loop to calculate grades.

grades = [35, 67, 98, 100, 100]

total = 0

amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)