def add(x, y):
    print(x + y)


add(5, 8)

# What you should not do is this:

# default_y = 3

# def add(x, y=default_y):
#     sum = x + y
#     print(sum)

# add(2)

# # This should return 5

# and even if you do: default_y = 4
# add(2) 

# this again do give 5. as when fun gets decleared this is at that time it retains those values.