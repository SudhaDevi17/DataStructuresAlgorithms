def powerset(array):
    # Write your code here.
    subsets = [[]]
    for ele in array :
        for i in range(len(subsets)):
            currset = subsets[i]
            subsets.append(currset+[ele])
    return subsets

print(powerset([1,2]))