#Python3
def poke(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)
