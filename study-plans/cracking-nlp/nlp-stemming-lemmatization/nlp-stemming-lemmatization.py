def stem_and_lemmatize(word: str, lemma_dict: dict) -> dict:
    """
    Returns a dictionary with string values stem and lemma.
    """
    result = dict()
    result["lemma"] = lemma_dict.get(word,word)
    # Porter Stemming
    if len(word) >= 5 and word[-3:] == "ing":
        word = word[:-3]

    if len(word) >= 4 and word[-2:] in ["er","ly" , "ed"]:
         word = word[:-2]

    if not word.endswith("ss") and word.endswith("s") and len(word) >= 3:
        word = word[:-1]

    if word.endswith("tion") and len(word) >= 5:
        word = word[:-3]+"e"
    result["stem"] = word

    return result 
    
    
    