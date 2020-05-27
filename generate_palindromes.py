

def generate_palindromes(limit):

    lst = []
    for i in range(limit, 0, -1):
        if str(i) == str(i)[::-1]:

            lst.append(i)
            lst.sort()

        if len(lst) == 15:
            break

    return lst
