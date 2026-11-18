import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    data = pd.DataFrame(data = data)
    rows , cols ,columns = *data.shape , data.columns.to_list()
    
    dtypes = data.dtypes.astype(str).to_dict()

    return {
        "rows" : rows , 
        "cols" : cols , 
        "columns" : columns ,
        "dtypes" : dtypes,
        "total_values" : rows*cols
    }
    
