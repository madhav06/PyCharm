
#Conditional expressions (aka 'ternary')¶
#Setting a variable to either of two values depending on some condition is a pretty common pattern.


def quiz_message(grade):
    if grade < 50:
        outcome = 'failed'
    else:
        outcome = 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


def quiz_message2(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)

quiz_message(80)
quiz_message2(45)