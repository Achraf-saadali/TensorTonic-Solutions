import pandas as pd

def change_dtype(data: dict, column: str, target_type: str) -> list:
    """
    Returns [dtypes_before, dtypes_after], both dictionaries of column names to dtype strings.
    """
    df = pd.DataFrame(data = data)


    dtypes_b = {column : str(df[column].dtypes) for column in df.columns }

    df = df.astype({column : target_type})

    dtypes_a = {column : str(df[column].dtypes) for column in df.columns }


    return [dtypes_b , dtypes_a ]
