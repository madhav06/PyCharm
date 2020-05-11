# Python 3

# Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

# next_edge(8, 10) ➞ 17

# next_edge(5, 7) ➞ 11

# next_edge(9, 2) ➞ 10




def next_edge(side1, side2):
	nxt = (side1 + side2) - 1
	print(nxt)

next_edge(8, 10)

next_edge(5, 7)

next_edge(9, 2)