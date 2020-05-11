# python 3

# Create a function that takes in three arguments (prob, prize, pay) and returns true if prob * prize > pay; otherwise return false.

# To illustrate, profitable_gamble(0.2, 50, 9) should yield true, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

# Examples
# profitable_gamble(0.2, 50, 9) ➞ True

# profitable_gamble(0.9, 1, 2) ➞ False

# profitable_gamble(0.9, 3, 2) ➞ True

def profitable_gamble(prob, prize, pay):
	if (prob*prize-pay) > 0:
		return True
	else:
		return False

if __name__ == '__main__':
	print(profitable_gamble(0.2, 50, 9))
	print(profitable_gamble(0.9, 1, 2))
	print(profitable_gamble(0.9, 3, 2))