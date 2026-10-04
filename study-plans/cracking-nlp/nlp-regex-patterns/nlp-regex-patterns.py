import re

def emails():
    #b is for the position of the epxression that match it
    regex = r"[A-Za-z0-9\.%_+-]+@[A-Za-z0-9\.-]+\.[A-Za-z][A-Za-z]+"
    return regex
def urls():
    regex = r"https?://\S*[^\s,.)!?;:]"
    return regex
def dates():
    # \d represent digigts
    # | is for alternatives
    # (? : A| B) grouping the alternatives
    regex = r"(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b"
    return regex
def money():
    regex = r"\$\d+(?:\.\d{2})?"
    return regex
def hashtags():
    # \w is for all alphanumeric characters including underscores .... 
    
    regex = r"#\w+"
    return regex
def extract_patterns(text: str, pattern_type: str) -> list:
    """
    Returns a list of matched strings.
    """
    
    operation = {
        "emails" :emails() , 
        "urls" : urls() ,
        "dates" : dates() ,
        "money" : money() , 
        "hashtags" : hashtags() 
        
    }
    
    if pattern_type not in operation.keys():
        return []
    return re.findall(operation[pattern_type] , text)
    