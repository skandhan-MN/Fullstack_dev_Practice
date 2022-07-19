class Solution:
    def minOperations(self, nums, x: int) -> int:
        if x == 0:
            return 0
        if min(nums)>x:
            return -1
        x_ = sum(nums)-x
        if x_==0:
            return len(nums)
        if x_<0:
            return -1
        
        start = 0
        max_len = 0
        tmp_sum = 0
        for end in range(len(nums)):
            tmp_sum += nums[end]
            if tmp_sum>x_:
                while tmp_sum >x_:
                    tmp_sum-=nums[start]
                    start+=1
            if tmp_sum == x_:
                max_len = max(max_len, end-start+1)
        return len(nums)-max_len

