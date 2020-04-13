
#Conditionals
#While useful enough in their own right, booleans really start to shine when combined with conditional statements, using the keywords if, elif, and else.

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)