mat = [[1, 2, 3,4], [4, 5,6,5], [7, 8, 9,6],[4,9,8,7]]
sum = 0
m = 4
n = 4
print("\nBoundary Matrix\n")
for i in range (0, m):
	for j in range (0, n):
		if (i == 0 or j == 0 or i == n-1 or j == n-1):
			print (mat[i][j], end = " ")
			sum = sum + mat[i][j]	
		else:
			print(end = " ")
print("\n")
print("\nSum of boundary is ", sum)