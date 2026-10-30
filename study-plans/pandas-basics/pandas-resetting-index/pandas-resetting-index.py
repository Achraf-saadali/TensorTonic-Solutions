import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    """
    Returns [columns_before_reset, columns_after_reset], both lists of strings.
    """


    df = pd.DataFrame(data = data)

    before = df.drop(columns = index_col)
    

    


    return [before.columns.to_list() , [index_col] +  before.columns.to_list()]


