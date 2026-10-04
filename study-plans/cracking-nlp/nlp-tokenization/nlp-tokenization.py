def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """
    
    
    print(text) 
    tokens = []

    i , j , n = 0 , 0 , len(text)

    while i < n :
            if text[i].isspace():
                tokens.append(text[j:i])
                while i < n and text[i].isspace():
                     i+=1
                j = i    
            elif not text[i].isalnum() and  text[i] != "_":
                if text[i] !="." or not text[j:i].isnumeric():
                    tokens.append(text[j:i])
                    tokens.append(text[i])
                    i +=1
                    j = i
            else :
                i+=1
    if j != i :
        tokens.append(text[j:i])
                

        
    
    return [token for token in tokens if len(token) > 0 ]
        
            
        
    
    
    
        
        
        
            
            

    