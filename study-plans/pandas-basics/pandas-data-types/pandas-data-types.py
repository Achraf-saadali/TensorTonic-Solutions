import pandas as pd

def data_types_overview(data: dict) -> dict:
    """
    Returns a dictionary with dtypes, type_counts, and num_columns.
    """

    data = pd.DataFrame(data = data)
    dtypes = data.dtypes.astype(str)

    type_counts = dtypes.value_counts().to_dict()

    num_columns = data.shape[1]

    return {
        "dtypes" : dtypes.to_dict() , 
        "type_counts" : type_counts , 
        "num_columns" : num_columns
    }
    
