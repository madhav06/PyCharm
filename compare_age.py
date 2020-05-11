# python 3

# Classes, Objects


# Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in the following format:

# {other_person} is {older than / younger than / the same age as} me.

# Examples

#p2 = Person("Joel", 36)
#p3 = Person("Lily", 24)
# p1.compare_age(p2) ➞ "Joel is older than me."

# p2.compare_age(p1) ➞ "Samuel is younger than me."

# p1.compare_age(p3) ➞ "Lily is the same age as me."


class Person:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if other.age > self.age:
			return other.name + 'is older than me.'
		elif other.age < self.age:
			return other.name + 'is younger than me.'
		else:
			return other.name + 'is the same age as me.'


#if __name__ == '__main__':
	
	#print(p2.compare_age(p1))
	#print(p1.compare_age(p3))