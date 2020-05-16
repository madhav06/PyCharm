
# Given an number, return a string of the word "Boom", which varies in the following ways:

# The string should include n number of "o"s, unless n is below 2 (in that case, return "boom").
# If n is evenly divisible by 2, add an exclamation mark to the end.
# If n is evenly divisible by 5, return the string in ALL CAPS.


# boom_intensity(4) ➞ "Boooom!"
# # There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)

# boom_intensity(1) ➞ "boom"
# # 1 is lower than 2, so we return "boom"

# boom_intensity(5) ➞ "BOOOOOM"
# # There are 5 "o"s and 5 is divisible by 5 (all caps)

# boom_intensity(10) ➞ "BOOOOOOOOOOM!"
# # There are 10 "o"s and 10 is divisible by 2 and 5



def explosion_intensity(n):
 if n < 2:
 	return ('boom')
 elif n%5 ==0 and n%2 == 0:
 	return ('B'+n*'O'+'M!')
 elif n%2 == 0:
 	return ('B'+n*'o'+'m!')
 elif n%5 == 0:
 	return ('B'+n*'O'+'M')
 else:
 	return ('B'+n*'o'+'m')
