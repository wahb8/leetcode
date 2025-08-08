# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

import copy

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]


def rotate(matrix):
    n = len(matrix) 
    matrix1 = copy.deepcopy(matrix) 

    for i in range(n):
        x = 0
        n = len(matrix)
        a = n
        n -= 1
         
        for l in range(a):
            matrix[i][l] = matrix1[n][i]
            n -= 1

        


    return matrix


print(a)
a[:] = zip(*a[::-1])
print(a[:])
print(a)


