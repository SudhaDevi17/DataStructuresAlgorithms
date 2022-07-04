
string = 'abaxyzzyxf'

def isPalindrome(test_string):
    left , right = 0 , len(test_string)-1
    while left< right:
        if test_string[left]!=test_string[right]:
            return False
        left+=1
        right-=1
    return True

def createSubstrings(string):
    longest_string = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            #print(i , j , substring, isPalindrome(substring))
            if isPalindrome(substring) and len(substring)>len(longest_string):
                longest_string = substring
    #print(longest_string)
    return longest_string
#print(createSubstrings(string))
# time O(n3) | spce O(n)



