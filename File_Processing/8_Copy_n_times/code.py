#Python3

#Copy n-times Exercise
#Python3

# Hint: Create a "with" block where you open the file in 'a+' mode. Put the cursor on top of the file. Read the file storing its content in a variable,
#put the cursor on top of the file, write the content, write the content.

with open("data.txt", "a+") as filehorse:
    filehorse.seek(0)
    content = filehorse.read()
    filehorse.seek(0)
    filehorse.write(content)
    filehorse.write(content)
