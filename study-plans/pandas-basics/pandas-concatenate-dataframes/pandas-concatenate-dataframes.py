import pandas as pd

def concat_dataframes(dfs: list) -> list:
    """
    Returns [shape, data], with shape [rows, columns] and data a dictionary of lists.
    """

    
    dfs = [pd.DataFrame(df) for df in dfs ]

    concatenated = pd.concat(dfs)


    

    return [list(concatenated.shape) , concatenated.to_dict("list")] 
    
