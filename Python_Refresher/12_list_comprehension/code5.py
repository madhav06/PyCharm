# Without list comprehensions, using general loops only
friends = ["Rolf", "Sam", "Samantha", "Jen", "Saurabh"]
starts_with_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_with_s.append(friend)


print(starts_with_s)


# Using with list comprehensions:

friends = ["Rolf", "Sam", "Samantha", "Jen", "Saurabh"]

starts_with_s = [friend for friend in friends if friend.startswith("S")]

print(starts_with_s)