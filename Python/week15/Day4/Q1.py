class Solution:
    def minMoves(self, nums) -> int:
        sum=0
        m = min(nums)
        i = nums.index(m)
        for j in range(len(nums)):
            if(i==j):
                continue
            else:
                sum = sum+nums[j]-nums[i]
        return sum