import pandas as pd

def select_columns(data: dict, columns: list) -> dict:
    """
    Returns a dictionary of value lists in the requested column order.
    """
    data = pd.DataFrame(data = data )

    return data[columns].to_dict("list")
