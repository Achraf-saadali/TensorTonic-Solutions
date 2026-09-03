def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here
    n = len(series)
    if n  <= 1:
        return series
    myList = [0.0]*(n-1)

    for i in range(n-1):
        if series[i] != 0 :
            myList[i] = ((series[i+1] - series[i]) / series[i])   



    return myList