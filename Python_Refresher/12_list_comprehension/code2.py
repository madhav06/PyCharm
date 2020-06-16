# finding common numbers from two lists using for loop:

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = []

for a in list_a:
    for b in list_b:
        if a == b:
            common_num.append(a)

print(common_num)    # Output: [2, 3, 4]


# finding common numbers from two lists using list comprehensions:

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [(a) for a in list_a for b in list_b if a == b]

print(common_num)    # Output: [2, 3, 4]