# Create a function that turns a list of words into a comma separated list,
# where the last word is separated by the word "and".
#
#
# words_to_sentence(["edabit"]) ➞ "edabit"
#
# words_to_sentence(["Hello", "", "Bye"]) ➞ "Hello and Bye"
#
# words_to_sentence(["Hello", "Bye", "See you soon"]) ➞ "Hello, Bye and See you soon"


def words_to_sentence(words):

    # Exceptions
    if words == None:
        return ''

    if len(words) == 1:
        return words[0]

    if len(words) < 1:
        return ''

    # Regular Code
    newwords = []

    for word in words:

        if word == None or word == '':
            continue
        else:

            newwords.append(word)


    words = newwords
    del newwords

    tr = ', '.join(words[:-1] + ' and ' + words[-1])

    return tr
    
