import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    data = pd.DataFrame(data = data)

    filtered_data = data.loc[data[column] > threshold ,]

    return {
        "filtered_data" : filtered_data.to_dict("list") , 
        "count" : filtered_data.shape[0]
    }
