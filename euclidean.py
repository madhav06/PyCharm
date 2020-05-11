# python 3

# Create a recursive function that returns the GCD between two positive numbers using the Euclidean Algorithm.

# euclidean(8, 6) ➞ 2

# euclidean(25, 5) ➞ 5

# euclidean(49, 14) ➞ 7


def euclidean(a, b):
	if a < b:
		return euclidean(b, a)
	r = a%b

	if r == 0:
		return b
	else:
		a = b
		b = r

	return euclidean(a, b)

if __name__ == '__main__':
	print(euclidean(49, 14))