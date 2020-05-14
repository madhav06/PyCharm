
# In music, cadences act as punctuation in musical phrases, and help to mark the end of phrases. Cadences are the two chords at the end of a phrase. The different cadences are as follows:

# V followed by I is a Perfect Cadence
# IV followed by I is a Plagal Cadence
# V followed by Any chord other than I is an Interrupted Cadence
# Any chord followed by V is an Imperfect Cadence
# Create a function where given a chord progression as a list, return the type of cadence the phrase ends on.



'''Examples
find_cadence(["I", "IV", "V"]) ➞ "imperfect"

find_cadence(["ii", "V", "I"]) ➞ "perfect"

find_cadence(["I", "IV", "I", "V", "vi"]) ➞ "interrupted"
Notes
Return strings all in lowercase.
Only focus on the last two chords of a progression.
Return "no cadence" if none of the criterea match up.
I is a capital i not a lowercase L. '''

def find_cadence(chords):
	if chords[-2] == 'V':
		return 'perfect' if chords[-1] == 'I' else 'interrupted'
	if chords[-2:] == ['IV', 'I']:
		return 'plagal'
	if chords[-1] == 'V':
		return 'imperfect'
	return 'no cadence'


# alternate solution 
'''
def find_cadence(chords):
	if chords[-2] == 'V' and chords[-1] == 'I':
		return 'perfect'
	elif chords[-2] == 'V' and chords[-1]!= 'I':
		return 'interrupted'
	elif chords[-2] == 'IV' and chords[-1] == 'I':
		return 'plagal'
	elif chords[-1] == 'V':
		return 'imperfect'
	else:
		return 'no cadence'

'''

