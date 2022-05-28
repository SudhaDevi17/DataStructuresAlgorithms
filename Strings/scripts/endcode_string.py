def caesarCipherEncryptor(string, key):
    alphabets = {'a':1 , 'b':2, 'c':3, 'd':4, 'e':5,'f':6, 'g':7, 'h':8,
                 'i':9, 'j':10,'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
                 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
                 'w':23, 'x':24, 'y':25, 'z':26
                 }
    res =[]
    for c in string:
        val = alphabets[c]+key
        char = getChar(alphabets , val )
        if char:
            res.append(char)

    return ''.join(res)

def getChar(alphabets , val ):
# TODO : remove the forloop
    for k,v in alphabets.items():
        val = val if val <=26 else val%26
        if v==val:
            return k

print(caesarCipherEncryptor('xyz', 2))
print(chr(97))
print(ord('a'))