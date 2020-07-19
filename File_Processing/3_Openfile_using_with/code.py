#Python3
with open("the_pool_tears.txt") as myfile:
    content = myfile.read()

print(content)

# Note: different filepaths
# So, if we happen to work or open a file from different directory like: "down_the_rabbit.txt",
# then we need to specify the file path for the same to access the directory and open the file
# and work on it.
# for example: we should write: open("2_Closing_a_file/down_the_rabbit.txt").
