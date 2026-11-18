import pandas as pd

def apply_transform(data: dict, column: str, operation: str) -> dict:
    """
    Returns the original column lists plus the target column with a _transformed suffix.
    """
    df = pd.DataFrame(data = data )
    
    col_transf = column+"_transformed"

    mydf = df.loc[:,[column]]

    if operation == "normalize":
        df[col_transf] = mydf.apply(lambda col : ((col - col.min())/(col.max() - col.min()))  , axis = 0).round(4)

    elif operation == "double":
        df[col_transf] = mydf.apply(lambda col : 2*col  , axis = 0).round(4)
    else  :

        df[col_transf]  = df[column].transform(operation)
        
    if operation == "rank":
        df[col_transf] = df[col_transf].astype(int)
        
    
    
        


    return df.to_dict("list")


def normalize(x : pd.DataFrame,column):

    

    return round((x - min)/(max - min) , 4)


def double(x : pd.DataFrame , column):
    return round(2*x[column] , 4)


    

    
