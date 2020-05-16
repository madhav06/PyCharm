# Create a function that takes a number (step) as an argument and 
#returns the amount of boxes in that step of the sequence.

# Step 0: Start with 0
# Step 1: Add 3
# Step 2: Subtract 1
# Repeat Step 1 & 2 ...

# Examples:
# box_seq(0) ➞ 0

# box_seq(1) ➞ 3

# box_seq(2) ➞ 2
# Notes:
# Step (the input) is always a positive integer (or zero).

def box_seq(step):
	if step%2 != 0:
		return step+2
	else:
		return step