''' The next iteration of Mario Kart will feature an extra-infuriating new item, the Purple Shell. 
When used, it warps the last place racer into first place and the first place racer into last place. 
Complete the function below to implement the Purple Shell's effect. '''


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    # One slick way to do the swap is x[0], x[-1] = x[-1], x[0].
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    pass

# Check your answer
#q3.check()