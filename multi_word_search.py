


#A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

#Your function should meet the following criteria:

#Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, 
#you would not include the string “enclosed.”
#She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” 
#would be included when the keyword is “closed”
#Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. 
#But you can assume there are no other types of punctuation.

#Once we done that(word_search.py) program. We 

#3.
#Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.

#You're encouraged to use the word_search function you just wrote when implementing this function. Reusing code in this way makes your programs more robust and readable - 
#and it saves typing!) 



def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices
    
    pass

# Check your answer
#q3.check()