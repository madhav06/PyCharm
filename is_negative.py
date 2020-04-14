

#Single line if-then syntax using chain comparison?

#The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.

#owever, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.

#See if you can come up with an equivalent body that uses just one line of code, and put it in the function concise_is_negative.
# (HINT: you don't even need Python's ternary syntax)

def is_negative(number):
    if number < 0:
        return True
    else:
        return False


def concise_is_negative(number):
    pass  # Your code goes here (try to keep it to one line!)
    return True if (number < 0) else False


# Check your answer
#q4.check()
