
#
# Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.
#
#
# divides_evenly(98, 7) ➞ True
# # 98/7 = 14
#
# divides_evenly(85, 4) ➞ False
# # 85/4 = 21.25


def divides_evenly(a, b):

    if (a % b == 0):
        return True

    else:
        return False


# # using lambda 
#
#
# divides_evenly = lambda a, b: a % b < 1
