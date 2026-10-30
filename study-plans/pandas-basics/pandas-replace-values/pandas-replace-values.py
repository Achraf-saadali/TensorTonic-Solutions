import pandas as pd

def replace_values(data: dict, column: str, old_val: object, new_val: object) -> dict:
    """
    Returns data as a dictionary of updated lists and count as an integer.
    """
    df  = pd.DataFrame(data = data )

    count = df.loc[df[column]== old_val,[column]].count().tolist()[0]
    

    df.loc[df[column]== old_val, [column]] = new_val


    data = df.to_dict(orient = "list")






    return {
        "data" : data , 
        "count" : count 
    }
