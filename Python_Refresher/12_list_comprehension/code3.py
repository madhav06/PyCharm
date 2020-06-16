# List comprehensions can also be used to iterate over strings:

list_a = ["Hello", "World", "In", "Python"]

small_list_a = [str.lower() for str in list_a]

print(small_list_a)    # Output: ['hello', 'world', 'in', 'python']