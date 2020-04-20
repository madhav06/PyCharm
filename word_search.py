

#2.


#A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

#Your function should meet the following criteria:

#Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, 
#you would not include the string “enclosed.”
#She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” 
#would be included when the keyword is “closed”
#Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. 
#But you can assume there are no other types of punctuation.

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indices = []
    for i, doc in enumerate(doc_list):
        words = doc.split()
        
        normalized = [word.rstrip('.,').lower() for word in words]
        
        if keyword.lower() in normalized:
            indices.append(i)
            
    return indices
    
    pass

# Check your answer
#q2.check()


