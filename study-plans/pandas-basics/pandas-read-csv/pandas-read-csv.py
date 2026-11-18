import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """

    data = pd.DataFrame(data = data)

    return {
        "data":data.to_dict(orient = "list") , 
        "shape" : list(data.shape) , 
        "columns" : data.columns.to_list()
    }
