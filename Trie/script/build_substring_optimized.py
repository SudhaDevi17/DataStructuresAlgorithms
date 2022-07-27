def longestPalindromeSubstring(string):
    currentLongest = [0,1]
    for i in range(1, len(string)):
        even = getLongestPalindromeIndex(string , i-1, i)
        odd = getLongestPalindromeIndex(string, i-1 , i+1 )

        longestSubstring = max(even , odd , key = lambda x  : x[1] - x[0])
        print(even, odd, longestSubstring)
        currentLongest = max(longestSubstring , currentLongest , key = lambda  x: x[1]- x[0])


        #print(longestSubstring, currentLongest)

    return currentLongest

def getLongestPalindromeIndex(string , left , right ):

    while left>= 0 and right <len(string):

        if string[left]!= string[right]:
            break
        left-=1
        right +=1
    #print(string[left+1:right], left , right)
    return [left +1 , right]
print(longestPalindromeSubstring('abaxyzzyxf'))

#https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
