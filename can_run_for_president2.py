
#Combining Boolean Values
#Python provides operators to combine boolean values using the standard concepts of "and", "or", and "not".
# And in fact, the corresponding Python operators use just those words: and, or, and not.
#With these, we can make our can_run_for_president function more accurate.





#problem, quote:

"""Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old

def can_run_for_president2(age, is_natural_american_citizen):
    return is_natural_american_citizen and (age >= 35)

print(can_run_for_president2(19, True))
print(can_run_for_president2(55, False))
print(can_run_for_president2(55, True))