import math

def tfidf(corpus: list) -> dict:
    """
    Returns a dictionary with vocab (token indices) and tfidf (float lists).
    """

    dictio = set()
    for doc in corpus : 
        for word in doc  :
            dictio.add(word)
    
    dictio = sorted(list(dictio))

    N = len(corpus)
    
    df_t = [sum(((t in doc for doc in corpus))) for t in dictio]

    idf_t = [math.log(N/df) for df in df_t]
    
    tf_t_d = [[doc.count(t) for t in dictio] for doc in corpus]

    tfidf = [[round(tf*idf , 4) for tf , idf in zip(tf_t , idf_t)] for tf_t in tf_t_d]


    vocabs = {}

    for index , word in enumerate(dictio):
        vocabs[word] = index 


    return {
        "vocab" : vocabs , 
        "tfidf" : tfidf
    }