
#The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog.
#We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order.

# --> when wants no onion

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

# --> when wants all toppings

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)

    """
    return ketchup and mustard and onion
    pass


# Check your answer
#q5.a.check()

# --> when want a plain hotdog

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    #we can also use this: return (not ketchup and not  mustard and not onion)
    return not (ketchup or mustard or onion)
    pass

# Check your answer
#q5.b.check()

# --> when want exactly one sauce

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    #use this: return bool(ketchup) ^ bool(mustard)
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass

# Check your answer
#q5.c.check()

# --> What happens if we call int() on a bool? Try it out in the notebook cell below.
# Can you take advantage of this to write a succinct "does the customer want exactly one topping?"? using int()


def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup + mustard + onion)==1
    pass

# Check your answer
#q6.check()