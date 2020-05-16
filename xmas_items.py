
# Throughout the 12 days of Christmas, my true love gave me in total 364 items.

# Create a function where given n days as an argument,
#  return the total amount of items received throughout those days as an integer.

#  xmas_items(12) ➞ 364

# xmas_items(3) ➞ 10

# xmas_items(31) ➞ 5456



# On the first day, 1 present.
# On the 2nd day, 1 + 3 = 4 presents
# On the 3rd day, 1 + 3 + 6 = 10 presents
# On the 4th day, 1 + 3 + 6 + 10 = 20 presents.

# These partial sums are called tetrahedral numbers, because they can be drawn as 3-dimensional triangular pyramids (tetrahedrons).


# Formula for nth tetrahedral number: 

# T(n) = (n * (n + 1) * (n + 2)) / 6

def xmas_items(n):
	return ( n * ( n + 1) * ( n + 2) ) // 6


# Alternate Sol

# def xmas_items(n):
# 	if n == 0:
# 		return 0
# 	tetrahedral_num = [n*(n+1) // 2 for n in range(1, n+1)]
# 	return sum(tetrahedral_num)
