# python3 
movies_watched = {"The Matrix", "Green Book", "Spiderman Homecoming"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've wqtched {user_movie} too! ")
else:
    print("I haven't watched that yet.")

# --

number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by 1.")
    else:
        ("Sorry, it's wrong!")

# --

# We could also do a transformation instead of checking multiple options.

number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input.lower() == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guesses correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")