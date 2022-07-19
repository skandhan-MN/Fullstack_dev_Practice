
def sortColors(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__" :

    nums = [2,0,2,1,1,0]
    ans = sortColors(nums)
    print(ans)