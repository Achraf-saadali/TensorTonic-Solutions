import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    """
    Returns null_counts as a dictionary of integers and cleaned_data as a dictionary of lists.
    """
    df = pd.DataFrame(data = data)
    
    null_counts = df.isnull().sum(axis = 0 )

    cleaned_data  = df.fillna(fill_value)

    return {
        "null_counts" : null_counts.to_dict() , 
        "cleaned_data" : cleaned_data.to_dict(orient = "list")
    }


    
    

    
    
    
