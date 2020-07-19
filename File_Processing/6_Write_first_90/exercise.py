# Create a first.txt file that contains the first 90 char of bear.txt

# Note that you should read the content of bear.txt with Python and extract 90 characters with python.
# and write those in first.txt in python.


#Python3

with open("americana.txt") as myfile:
    content = myfile.read()

with open("first.txt", "w") as myfile:
    myfile.write(content[:90])

    
