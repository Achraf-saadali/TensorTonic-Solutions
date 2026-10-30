import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    """
    Returns index_values and columns as lists, plus data as a dictionary of lists.
    """



    data =  pd.DataFrame(data = data ).set_index(index_col)
    index = data.index.to_list()
    columns = data.columns.to_list()

    return {
        "index_values" : index , 
        "columns" : columns , 
        "data" : data.to_dict("list")
    }
