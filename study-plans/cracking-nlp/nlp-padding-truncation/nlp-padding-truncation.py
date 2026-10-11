def pad_and_truncate(sequences: list, max_length: int, pad_value: int = 0) -> list:
    """
    Returns one integer list of length max_length per input sequence.
    """

    for i in range(len(sequences)):
        n = len(sequences[i]) 
        if n > max_length :
            #Trunctate if the sequence exceeds
            sequences[i] = sequences[i][:max_length]
        elif   n < max_length:
            #padding if the sequence is shorter
            sequences[i] = sequences[i] +[pad_value]*(max_length - n )


    return sequences