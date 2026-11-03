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

    n_sentences , m_dictio_words , p_sentence_tokens = len(corpus) , len(dictio) , len(corpus[0])
        

    vectors = []
    vocabs = { word : index for index , word in enumerate(dictio)}

    
    for document in corpus :
        doc_vec = [0]*len(dictio) 
        for token in document :
            doc_vec[vocabs[token]] += 1

        vectors.append(doc_vec)
            
            
            
                

    return {
        "vocab" : vocabs , 
        "vectors" : vectors 
    }
            
    