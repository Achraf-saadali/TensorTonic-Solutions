import pandas as pd

def select_column(data: dict, column: str) -> dict:
    """
    Returns a dictionary with values as a list and length as an integer.
    """
    values = data[column] 
    return {
        "values" : values, 
        "length" : len(values)
        
    }
