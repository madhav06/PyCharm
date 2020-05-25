# In this challenge, you are given a list and in turn, you must obtain a smaller list, following three steps:
#
# Split the list into two parts of equal length. If the given list has an odd length, then you have to eliminate the number in the middle of the list for obtaining two equal parts.
# Sum each number of the first part with each number of the reversed second part, obtaining a new single list having the same length of the previous two.
# Divide by two each number in the final list.
#
#
# antipodes_average([1, 2, 3, 4]) ➞ [2.5, 2.5]
# # Left part = [1, 2]
# # Reversed right part = [4, 3]
# # List resulting from the sum of each pair = [5, 5]
# # Each number is divided by two = [2.5, 2.5]

#
# def antipodes_average(lst):
#
#     l = len(lst)//2
#     a = lst[:l]
#     b = lst[-l:][::-1]
#
#     return [(a[i] + b[i])/2 for i in range(l)]

# Alternative solution

def antipodes_average(lst):
    return [(lst[i] + lst[-i-1])/2 for i in range (len(lst)//2)]
