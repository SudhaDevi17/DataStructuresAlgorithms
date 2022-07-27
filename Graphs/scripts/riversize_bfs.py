M = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
def exploreNeighbors(i,j, M, visited):
    R, C = len(M), len(M[0])
    connect = []
    if i>0 and not visited[i-1][ j]:
        connect.append([i-1 , j ])
    if i< R-1  and  not visited[i+1][ j]:
        connect.append([i+1 , j ])
    if j>0 and not visited[i][ j-1 ] :
        connect.append([i , j-1])
    if  j < C-1 and not visited[i][j+1 ] :
        connect.append([i, j+1])
    return connect


def traverse(i,j, M, visited, riversize):
    currentRiverSize = 0
    nodesToExplore = []
    nodesToExplore.append([i,j])
    while len(nodesToExplore):
        node = nodesToExplore.pop(0)
        i,j =node[0], node[1]

        # if 0 and visited
        if visited[i][j] :
            continue
        # if non-zero and not visited
        visited[i][j] = True
        if M[i][j] == 0 :
            continue
        currentRiverSize+=1

        nodes_list = exploreNeighbors(i, j ,M, visited)
        for node in nodes_list:
            nodesToExplore.append(node)
    if currentRiverSize>0:
        riversize.append(currentRiverSize)
    #return riversize
def riversizecal(M ):
    visited = [[False for value in row  ] for row in M]
    riversize = []

    for row in range(len(M)):
        for col in range(len(M[0])):
             if visited[row][col]:
                 continue
             traverse(row, col, M , visited, riversize )
    return riversize

print(riversizecal(M))
#print(M[4][2])