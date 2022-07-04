A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1], [2], [3]]

C = [[0]*len(B[0]) for row in range(len(A))]

for rowA in range(len(A)):
    for colB in range(len(B[0])):
        for rowB in range(len(B)):
            C[rowA][colB] = A[rowA][rowB] * B[rowB][colB]

# print(C)
# print(len(C), len(C[0]))
#
print(28%26)
