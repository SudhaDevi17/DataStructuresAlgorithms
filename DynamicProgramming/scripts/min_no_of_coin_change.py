def minNumberOfCoinsForChange(n, denoms):
    """
    :param n: target amount of money
    :param denoms: coin denominations
    :return: numbers of coins needed to make change(to sum up to the given target)
    """

    if not denoms:
        return -1

    res = [float('inf') for _ in range(n+1)]
    res[0]=0

    for t in range(1,n+1):
        for denom in denoms:
            if denom<=t:
                res[t] = min(res[t], res[t-denom]+1)

    return res[-1] if res[-1]!= float('inf') else -1
# time : O(n*d)
# space: O(n)
