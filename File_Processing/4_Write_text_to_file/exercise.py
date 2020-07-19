#Reading and Processing Text
# Read a .txt file and print out the first 90 characters of its content.

# Hints: The file.read() method returns a string.
# You can use [:90] to extract the first 90 characters from that string.


#Python3
with open("little_bill.txt") as myfile:
    content = myfile.read()
    myfile.close()
print(content[:90])
