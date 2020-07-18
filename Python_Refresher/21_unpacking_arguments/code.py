def multiply(*args):
    total = 1
    for arg in args:
        total = toal * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:"
        return "No vaild operator provided to apply(). "


print(apply(1, 3, 6, 7, operator="+"))