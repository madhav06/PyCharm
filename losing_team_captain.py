
'''You are analyzing sports teams. Members of each team are stored in a list. 
The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. 
These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.
 Complete the function below to select the captain of the worst team. '''

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    
    team_best = [['Paul', 'John', 'Ringo', 'George'], ['Jen', 'Jamie', 'Krunal']]   # team1 , team2 = (coach, captain, players..), (coach, captain, players...)
    
    return teams[-1][1]    #selecting worst team then selecting their captain 
    
    
    pass

# Check your answer
#q2.check()