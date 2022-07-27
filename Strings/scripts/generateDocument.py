def generateDocument(characters, document):
    # matches unique character frequencies among 2 strings
    # to find whether a doc can be created from characters or not

    from collections import Counter
    if not len(characters):
        return False
    charCounter , docCounter = Counter(characters) , Counter(document)
    #print('a' in charCounter.keys())
    for key,val in docCounter.items():

        docFreq = val
        if key not in charCounter.keys():
            return False

        elif key in charCounter.keys():
            charFreq= charCounter[key]
            if docFreq> charFreq:
                return False

    return True

print(generateDocument("aheaolabbhb", "hello"))