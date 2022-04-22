
def riverSizes(matrix):
    # DFS - Unsolved , how to maintain a variable value ?
    # alternate - can be implemented using stack also
    # time and space complexity is not clear
    # this is probably not the most optimized solution
    # we can also implement it using LRU_cache
    # still edge cases are there because of which I am unable to handle corner cases

    visited= [[False for val in row] for row in matrix]
    size =[]
    res = 0
    W,H= len(matrix), len(matrix[0])
    for r in range(W):
        for c in range(H):

            if visited[r][c]:
                continue
            if matrix[r][c]==0:
                visited[r][c]= True
                continue
            if matrix[r][c]:
                res = dfs(r, c , matrix, visited ,size,  0 )
                print(res)
                if res is not None:

                    size.append(res)

    return size if len(size)>1  else []

def dfs(i,j,M, visited,size ,currsize):

    if M[i][j]==0:
        visited[i][j]= True
        if currsize>0:
            #size.append(currsize)
            size.append(currsize)
            currsize  = 0
        # exit
    if visited[i][j]:
        exit

    if M[i][j] and not visited[i][j]:
        visited[i][j] = True
        currsize+=1
        # if currsize>0 and i == len(M)-1 or j == len(M[0])-1:
        #     return size.append(currsize)
    # explore neighbors
    if i>0 and not visited[i-1][j]:
        dfs(i-1 , j , M, visited,size, currsize)
    if i < len(M)-1 and not visited[i+1 ][j]:
        dfs(i+1 , j , M, visited,size, currsize )
    if j>0 and not visited[i][j-1]:
        dfs(i , j - 1, M, visited,size, currsize )
    if j<len(M[0])-1 and not visited[i][j+1 ]:
        dfs(i , j +1, M, visited, size, currsize )
    if currsize>0 and not visited[i][j]:
        size.append(currsize)

    #return currsize



# m = [[1, 0, 0, 1, 0],
#      [1, 0, 1, 0, 0],
#      [0, 0, 1, 0, 1],
#      [1, 0, 1, 0, 1],
#      [1, 0, 1, 1, 0]]

m = [
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0]
]
print(riverSizes(m))