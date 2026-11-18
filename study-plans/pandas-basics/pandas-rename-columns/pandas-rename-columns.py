import pandas as pd

def rename_columns(data: dict, rename_map: dict) -> dict:
    """
    Returns a dictionary mapping renamed column names to their value lists.
    """
    data = pd.DataFrame(data = data).rename(columns = rename_map)

    return data.to_dict("list")
