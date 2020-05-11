# python3

# There are three towers. The objective of the game is to move all the disks over to tower #3, but you can't place a larger disk onto a smaller disk.

# Create a function that takes a number discs as an argument and returns the minimum amount of steps needed to complete the game.

# tower_hanoi(3) ➞ 7

# tower_hanoi(5) ➞ 31

# tower_hanoi(0) ➞ 0

# def tower_of_hanoi(discs):
# 	#print(discs)
# 	return (2**discs)-1

# tower_of_hanoi(3)

# tower_of_hanoi(5) 

# tower_of_hanoi(0) 



def tower_of_hanoi(discs):
	if discs < 3:
		return 0
	else:
		return ((2**discs)-1)


if __name__ == '__main__':
	
	print(tower_of_hanoi(3))
	print(tower_of_hanoi(5))
	
