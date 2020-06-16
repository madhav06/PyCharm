# find the squares of a number using the for loop:

numbers = [1, 3, 5, 7, 9, 11, 16, 20]
squares = []

for n in numbers:
    squares.append(n**2)

print(squares)   # Output: [1, 9, 25, 49, 81, 121, 256, 400]

# Finding squares using list comprehensions:

numbers = [1, 3, 5, 7, 9, 11, 16, 20]
squares = [n**2 for n in numbers]

print(squares)