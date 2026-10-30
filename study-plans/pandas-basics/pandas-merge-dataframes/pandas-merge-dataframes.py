import pandas as pd

def merge_dataframes(left: dict, right: dict, on: str, how: str) -> dict:
    """
    Returns a dictionary of merged column lists, with NaN for unmatched cells.
    """

    left , right = pd.DataFrame(data = left) , pd.DataFrame(data = right)

    return left.merge(right , on = on , how = how).to_dict("list")
