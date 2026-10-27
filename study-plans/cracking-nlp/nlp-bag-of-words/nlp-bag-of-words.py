def bag_of_words(corpus: list) -> dict:
    """
    Returns a dictionary with vocab (token indices) and vectors (integer count lists).
    """
    dictio = set()

    for L in corpus : 
        for word in L :
            dictio.add(word)

    dictio = list(dictio)
    dictio.sort()
    
        

    vectors = [[0 for i in range(len(dictio))] for j in range(len(corpus))]
    vocabs = {}

    for  index , word in enumerate(dictio):
        vocabs[word] = index 
    for i in range(len(corpus)):
        try:
            for j in range(len(corpus[i])):
                vectors[i][vocabs[corpus[i][j]]]+= 1
        except Exception as e :
            pass
                

    return {
        "vocab" : vocabs , 
        "vectors" : vectors 
    }
            
    