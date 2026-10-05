import re
def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """
    

    return re.findall(r"\w+|[^\w\s]" , text)
        
            
        
    
    
    
        
        
        
            
            

    