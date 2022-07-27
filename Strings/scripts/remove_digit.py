class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        str_ = str(number)
        str_len = len(str_)
        res = []
        for i in range(str_len) :
            if str_[i]==digit:
                left  = i
                right = (len(str_)-left +1 +1)
                if right==str_len-1:
                    temp = int(str(number[0:right-1]))
                elif left==0:
                    temp = int(str(number[1::]))
                else:
                    temp = int(str(number[:left])+str(number[right+1:]))
                res.append(temp)

        return max(res)

s = Solution()
# print(s.removeDigit("123" , "3"))
#
# print(s.removeDigit("551" , "5"))
#
# print(s.removeDigit("1231", "1"))

print(s.removeDigit("13333", "3"))
# s = "123"
# i = 2
# left =2
# right = len(s)-left+2
# print(s[:left])
# print(s[right:])
