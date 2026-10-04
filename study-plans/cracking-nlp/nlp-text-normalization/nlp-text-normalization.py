import re






def text_normalize(text: str, operations: list) -> str:
    """
    Returns the normalized string.
    """
    
    operation_registry = {
        "lowercase" :  lowercase , 
        "remove_punctuation" : remove_punctuation , 
        "remove_digits" : remove_digits ,
        "strip" : strip , 
        "remove_digits" : remove_digits ,
        "collapse_whitespace" : collapse_whitespace
        
    } 

    for operation in operations:
        text = operation_registry[operation](text)

    return text

#HELPER FUNCTIONS 
def  lowercase(word):
    return word.lower()

def strip(word):
    return word.strip()

def remove_punctuation(word):
    return "".join(char for char in word if  char.isalnum() or char.isspace() )

    return word
def remove_digits(word):

    return "".join(char for char in word if not char.isdecimal())

    return word
def collapse_whitespace(word):

    i , n = 0 , len(word) 
    result = ""
    while i < n:
        if word[i].isspace():
            result +=" "
            while i < n and word[i].isspace():
                i +=1
            
        else :
            result += word[i]
            i += 1

    return result

    
            