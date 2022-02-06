def numberOfWaysToMakeChange(n, denoms):
    if not n:
        return 0
    changes = [0 for _ in range(n+1)]

    changes[0] = 1
    for i in range(1, n+1):
        for denom in denoms:
            if denom<=i:
                #changes[i] +=
                changes[i] =  changes[i]+changes[i-denom]
    print(changes[n])

    return changes[n]

numberOfWaysToMakeChange(6, [1,5])
#numberOfWaysToMakeChange(5, [1,5, 10 ,25])