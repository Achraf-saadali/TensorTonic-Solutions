import pandas as pd

def multi_groupby(data: dict, group_cols: list, value_col: str, aggfunc: str) -> dict:
    """
    Returns a dictionary of lists for the grouping columns and aggregated value column.
    """
    df = pd.DataFrame(data = data)
    df = df.groupby(by = group_cols , as_index = False).agg({value_col : aggfunc})

    return df.to_dict("list")

    
