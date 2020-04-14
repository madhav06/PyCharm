#Modify the definition in the cell below to correct the grammar of our print statement.
#(If there's only one candy, we should use the singular "candy" instead of the plural "candies")

print("current O/P:")
#Splitting 91 candies
#Splitting 1 candies'''


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

   ## >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3


to_smash(91)
to_smash(1)
print("\n")
print("Updated O/P:")


def to_smash_split(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

   ## >>> to_smash(91)
    1
    """
    if(total_candies==1):
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")


    return total_candies % 3


to_smash_split(91)
to_smash_split(1)