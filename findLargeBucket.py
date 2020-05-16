# Create a function that takes a list of numbers. Return the largest number in the list.

# findLargestNum([4, 5, 1, 3]) ➞ 5

# findLargestNum([300, 200, 600, 150]) ➞ 600

# findLargestNum([1000, 1001, 857, 1]) ➞ 1001


def findLargeBucket(nums):
	largest = nums[0]
	for i in nums:
		if i > largest:
			largest = i
	return largest
	#print(largest)

	findLargeBucket([300, 200, 600, 150])
	findLargeBucket([1000, 1001, 857, 1])
