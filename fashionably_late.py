
''' We're using lists to record people who attended our party and what order they arrived in. 
For example, the following list represents a party with 7 guests, 
in which Adela showed up first and Ford was the last to arrive: '''

# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. 
#However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.

#Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.


def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    index = arrivals.index(name)
    
    if index >= len(arrivals)/2 and index != len(arrivals)-1:

        return True

    else:

        return False
    pass

# Check your answer
#q5.check()