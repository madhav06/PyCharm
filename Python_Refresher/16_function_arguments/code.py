# def add(x,y):
#     pass, we are passing two parametes by creating 2 variables.


def say_name(first, last):
    print(f"Hello, {first} {last}.")



say_name("Madhav", "Nandan")

say_name("Kasturi", "Priya")



# another example:

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("This is not divide.")

divide(15, 0)
divide(25, 5)