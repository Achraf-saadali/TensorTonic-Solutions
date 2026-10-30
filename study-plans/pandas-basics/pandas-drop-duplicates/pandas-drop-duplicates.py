import pandas as pd

def drop_duplicates(data: dict) -> list:
    """
    Returns [rows_before, rows_after, cleaned_data], with integer counts and a dictionary of lists.
    """
    df = pd.DataFrame(data = data )

    drop_duplicates = df.drop_duplicates(subset = df.columns , keep = "first")


    return [df.shape[0] , drop_duplicates.shape[0] , drop_duplicates.to_dict(orient = "list")]




    return 
