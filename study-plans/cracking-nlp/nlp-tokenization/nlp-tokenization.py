def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """
    
    
    #My List of tokens 
    tokens = []

    i , j , n = 0 , 0 , len(text)

    while i < n :
            #Dividing and ignoring On whitespaces   
            if text[i].isspace():
                tokens.append(text[j:i])
                while i < n and text[i].isspace():
                     i+=1
                j = i   
            #Dividing On Non alphanumerical 
            #But keeping  token intact on a hyphen and when the dot is previewd by a number 
            elif not text[i].isalnum() and  text[i] != "_":
                if text[i] !="." or not text[j:i].isnumeric():
                    tokens.append(text[j:i])
                    tokens.append(text[i])
                    i +=1
                    j = i
            else :
                i+=1
    
    tokens.append(text[j:i])
                

        
    
    return [token for token in tokens if len(token) > 0 ]
        
            
        
    
    
    
        
        
        
            
            

    