#Python3

myfile = open("down_the_rabbit.txt")
content = myfile.read()
myfile.close()
# if we further do: myfile.read(), we will get Traceback error because file has closed.
print(content)
