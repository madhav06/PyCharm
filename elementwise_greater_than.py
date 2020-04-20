
#R and Python have some libraries (like numpy and pandas) compare each element of the list to 2 (i.e. do an 'element-wise' comparison) and give us a list of booleans like [False, #False, True, True].

#Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.


"""Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

     '''uncomment this to use one-liner code: And here's the list comprehension version:

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]   '''

    pass

# Check your answer
#q2.check()