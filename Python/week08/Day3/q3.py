A = [[1,1,0],[1,0,1],[0,0,0]]

class Solution:
    def flipAndInvertImage(self, A):
        length = len(A)
        for i in range(length):
            for j in range(length-1,-1,-1):
                if A[i][j] == 1:
                    A[i].append(0)
                else:
                    A[i].append(1)
        rtype = [i[length:] for i in A]
        return  rtype
a = Solution()
q = a.flipAndInvertImage(A)
print("q = ",q)