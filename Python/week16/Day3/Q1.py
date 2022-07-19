class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2 :
            return
        
        initial = nums[0]
        pointer =0
        for num in nums :
            if num > initial:
                pointer += 1
                nums[pointer] = num
                initial = num
        
        return(pointer+1)