def maxSubsetSumNoAdjacent(array):
    """
    :param array: positive integers
    :return: the maximum sum of non adjacent elements in an array
    """
    if not array:
        return 0
    res1, res2= 0,0
    n = len(array)


    res2= array[0]

    if n>=2:
        res1= max(array[0], array[1])

    if n>=2:
        for i in range(2,n):
            temp = max(array[i]+res2, res1)
            res2=res1
            res1=temp

    return max(res1, res2)
