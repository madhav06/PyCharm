#ccheck if a number is odd by checking that the modulus with 2 returns 1 using comparisons

#use == instead of = when making comparisons. If you write n == 2 you are asking about the value of n.

def is_odd(n):
    return (n % 2) == 1

#we are using booleans here
print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))