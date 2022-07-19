class Solution:

    def climbStairs(self, n: int) -> int:
        ot=[0,1]
        for i in range(1,n+1):
            s=ot[i-1]+ot[i]
            ot.append(s)

        return max(ot)


if __name__ =="__main__":
    ans = Solution


