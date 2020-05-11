# python 3

# Create a function that takes a string and returns a string with its letters in alphabetical order.

# alphabet_soup("hello") ➞ "ehllo"

# alphabet_soup("edabit") ➞ "abdeit"

# alphabet_soup("hacker") ➞ "acehkr"

# alphabet_soup("geek") ➞ "eegk"

# alphabet_soup("javascript") ➞ "aacijprstv"


def alphabet_soup(txt):
 return "".join(sorted(txt))

if __name__ == '__main__':
	print(alphabet_soup("geek"))
	print(alphabet_soup("javascript") )