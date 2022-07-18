def groupAnagrams(words):
    """
    :param words: list of anagrams
    :return: a list of similar anagrams into a bucket
    O(n*log(word)*word + O(n)*O(k) time complexity | O(n+m) space complexity
    - space for the auxillary space and dictionary created
    - time for 1 forloop and sort function, k for length of substring
    """
    aux_words = [""]*len(words)
    for i,word in enumerate(words):
        aux_words[i] = ''.join(sorted(word))
    word_map = {}
    from collections import defaultdict
    #word_map = defaultdict()
    for idx, string in enumerate(aux_words):
        if string not in word_map:
            word_map[string] = []
        word_map[string].append(idx)

    res = []
    for val in word_map.values():
        bucket = [words[i] for i in val]
        res.append(bucket) # O(1)
    return res

def optimizedGroupAnagrams(words):
    """
    :param words: list of anagrams
    :return: a list of similar anagrams into a bucket
    O() time complexity | O() space complexity
    """
    anagrams = {}
    for word in words:
        SortedWord = ''.join(sorted(word))
        if SortedWord in anagrams:
            anagrams[SortedWord].append(word)
        else:
            anagrams[SortedWord] = [word]
    return list(anagrams.values())

# result = groupAnagrams(words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"])
# print(result)

result = optimizedGroupAnagrams(words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"])
print(result)