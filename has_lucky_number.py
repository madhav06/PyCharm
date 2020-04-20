

"""Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """

def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    # We've exhausted the list without finding a lucky number
    return False
# Check your answer
#q1.check()