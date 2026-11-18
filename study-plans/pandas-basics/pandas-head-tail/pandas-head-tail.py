import pandas as pd

def head_tail(data: dict, n: int) -> dict:
    """
    Returns head and tail as dictionaries mapping columns to value lists.
    """
    data = pd.DataFrame(data = data) 
    
    head , tail = data.iloc[:n,] , data.iloc[:-n-1:-1, ].iloc[::-1,]

    return {
        "head" : head.to_dict(orient = "list") ,
        "tail" : tail.to_dict(orient = "list")
    }
