

# John is playing a dice game. The rules are as follows.

# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!

# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.

# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21

# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0

# dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27


#initialize

def dice_game(lst):
	Score = 0

	for i in range(len(lst)):
		if lst[i][0] == lst[i][1]:
			Score = 0
			break
		else:
			Score += lst[i][0] + lst[i][1]

	return Score

	

	