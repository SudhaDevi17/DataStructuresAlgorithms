def runLengthEncoding(string):
    # need to write a clean code here
    resultString=[]
    runLength= 1

    for i in range(1,len(string)):
        currCharacter = string[i]
        previousCharacter=  string[i-1]
        if  currCharacter != previousCharacter or runLength==9:
            resultString.append(f"{runLength}{previousCharacter}")
            runLength=0
        runLength+=1
    resultString.append(f"{runLength}{string[len(string)-1]}")
    return "".join(resultString)

print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))