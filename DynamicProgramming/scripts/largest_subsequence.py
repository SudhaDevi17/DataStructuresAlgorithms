def maxSumIncreasingSubsequence(array):
    # Write your code here.
    n = len(array)
    idx = [None for _ in range(n) ]
    sums = [num for num in array]
    maxsum , maxsumidx = 0,0
    for i in range(n):
        currnum = array[i]

        for j in range(0 , i ):
            prevnum = array[j]
            if prevnum<currnum and currnum+sums[j]>= sums[i]:
                sums[i] = currnum+ sums[j]
                idx[i]= j
        if sums[i]>= sums[maxsumidx]:
            maxsumidx = i
    return [sums[maxsumidx] , getsubarray(array, idx, maxsumidx)]

def getsubarray(array, idx, curridx):
    res = []
    print(idx, curridx)
    while curridx is not None:
        num = array[curridx]
        res.append(num)
        curridx = idx[curridx]
    return list(reversed(res))

print(maxSumIncreasingSubsequence([10,70,20,30,50,11,30]))