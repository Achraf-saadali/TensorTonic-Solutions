def promote_model(models: list) -> str:
    """
    Returns the model name as a string.
    """
    
    return max(models ,
               key = lambda x : 
               (x["accuracy"] ,  - x["latency"] , x["timestamp"]) 
              )["name"]