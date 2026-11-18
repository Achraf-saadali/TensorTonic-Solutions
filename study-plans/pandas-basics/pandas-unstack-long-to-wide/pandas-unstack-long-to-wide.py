import pandas as pd

def unstack_to_wide(data: dict, index_col: str, columns_col: str, values_col: str) -> dict:
    """
    Returns identifier and category column lists, with NaN for missing pairs.
    """

    data = pd.DataFrame(data = data)

    return (data.pivot(index  = index_col , 
                      columns = columns_col , 
                      values = values_col)
        .reset_index(drop  = False).to_dict("list"))

