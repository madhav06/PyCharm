
# Create a function that returns True if the given circles are intersecting, otherwise return False. The circles are given as two lists containing the values in the following order:

# Radius of the circle.
# Center position on the x-axis.
# Center position on the y-axis.

# is_circle_collision([10, 0, 0], [10, 10, 10]) ➞ True

# is_circle_collision([1, 0, 0], [1, 10, 10]) ➞ False


''' for example:
Distance between centers C1 and C2 is calculated as
 C1C2 = sqrt((x1 - x2)2 + (y1 - y2)2).
There are three condition arises.
1. If C1C2 == R1 + R2
     Circle A and B are touch to each other.
2. If C1C2 > R1 + R2
     Circle A and B are not touch to each other.
3. If C1C2 < R1 + R2
      Circle intersects each other. 
'''


def is_circle_collision(c1, c2):
	x = c1[1] - c2[1]
	y = c1[2] - c2[2]

	distance = ((x**2) + (y**2)) ** 0.5

	if distance < (c1[0] + c2[0]):
		return True
	else:
		return False