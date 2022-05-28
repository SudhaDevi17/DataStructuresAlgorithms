def main():
    sequence = []
    virus_pattern = "coronavirus"#input()
    # number_of_ppl = 1#int(input())
    # for i in range(number_of_ppl):
    #     sequence.append(input())
    string = "crnvrs"

    getMatches(string, virus_pattern)

def getMatches(string , target):
    #print(len(string))
    virus_pointer = 0
    matches = 0
    ppl_pointer = 0

    while ppl_pointer <= len(string)-1:
        if string[ppl_pointer] == target[virus_pointer]:
            matches +=1
            ppl_pointer+=1
        virus_pointer+=1
    print(matches)
    output = 'POSITIVE' if matches == len(string) else 'NEGATIVE'
    print(output)
    return output




main()
