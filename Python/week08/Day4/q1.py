# Write a program to print sum of right diagonal of a matrix


MAX = 100
 
def printDiagonalSums(mat, n):

    secondary = 0
    for i in range(0, n):
        for j in range(0, n):
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]
         
    print("Secondary Diagonal:", secondary)
 
# Driver code
a = [[ 1,2,3],
     [ 4,5,6],
     [ 7,8,9]]
printDiagonalSums(a, 3)

b = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
printDiagonalSums(b, 3)

c = [[1,2],
     [3,4],
     [5,6]]
printDiagonalSums(c, 2)



