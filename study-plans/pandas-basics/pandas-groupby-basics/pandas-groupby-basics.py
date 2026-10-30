import pandas as pd

def groupby_basics(data: dict, group_col: str, value_col: str) -> dict:
    """
    Returns sum, mean, and count dictionaries keyed by group label.
    """
    df = pd.DataFrame(data = data )

    group = df.groupby(group_col)[value_col]

    count = group.count().to_dict()

    sum = group.sum().to_dict() 
    mean = group.mean().to_dict()

    return {"sum":sum,"mean" : mean , "count" : count}
