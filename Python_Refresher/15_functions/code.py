# def hello():   , this is how we define function.
#     print("Hello"), this is body of function

# hello(), we call it, to run the function.


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


user_age_in_seconds()

# now using our function in different way

# define our global variable first.

friends = []

def add_friend():
    friends.append("Rolf")


add_friend()
print(friends)
