friends = {"Hakim", "Ravi", "Dheeraj"}
abroad = {"Ravi", "Dheeraj"}

local_friends = friends.difference(abroad)
# print(local_friends)

bhopal = {"Amit", "Rajan", "Ankur", "Dhannu"}
dbg = {"Ravi", "Gopal", "Amar"}

friends = bhopal.union(dbg)
# print(friends)

art = {"Suman", "Gopal", "Anuradha", "Laluu", "Champakk"}
science = {"Amar", "Gopal", "Ganesh", "Champakk"}

both = art.intersection(science)
print(both)