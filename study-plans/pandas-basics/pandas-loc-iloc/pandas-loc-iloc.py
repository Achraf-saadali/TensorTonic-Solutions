import pandas as pd

def iloc_selection(data: dict, row: int, col: int) -> list:
    """
    Returns [element, row_values, col_values], with both value sequences as lists.
    """
    data = pd.DataFrame(data = data)
    
    row_values = data.iloc[row,:]
    col_values = data.iloc[:,col]

    return [data.iloc[row,col] ,
            
        row_values.to_list(),
            
        col_values.to_list()
    ]
    
