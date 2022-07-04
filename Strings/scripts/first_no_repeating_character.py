def firstNonRepeatingCharacter(string):
    # find the first non-repeating character in a string
    pair = set()
    n = len(string)-1
    if n==0:
        return 0
    for i,c in enumerate(string):
        if i+1 <= n:
            for j in range(i+1,len(string)):
                if string[i] not in pair:
                    if string[j]== string[i]:
                        pair.add(string[i])
                        continue
                    if j==n and string[j] != string[i]:
                        return i
        if i==n and string[i] not in pair:
            return i

    return -1

def firstNonRepeatingCharacteroptimized(string):
    # more optimized approach, use hash tables for easy lookups of repetition
    from collections import Counter

    character_freq = Counter(string)

    for i, c in enumerate(string):
        if character_freq[string[i]]==1:
            return i
        else:
            continue
    return -1

print(firstNonRepeatingCharacter('abcdcaf'))
print(firstNonRepeatingCharacter('faadabcbbebdf'))
print(firstNonRepeatingCharacter('ababac'))