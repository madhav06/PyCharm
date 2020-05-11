# python 3

# Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.

# frames(1, 1) ➞ 60

# frames(10, 1) ➞ 600

# frames(10, 25) ➞ 15000


def frames(minutes, fps):
	#return (minutes*fps*60)
	print(minutes*fps*60)
	
frames(1, 1)

frames(10, 1)

frames(10, 25)