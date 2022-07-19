def MaxAscendingSum(nums):
    count = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):

        if nums[i] > nums[i-1]:
            count += nums[i]
        else:
            count = nums[i]
        maxSum = max(maxSum, count)

    return maxSum


if __name__ == "__main__":

    nums = [10,20,30,5,10,50]
    res = MaxAscendingSum(nums)
    print(res)
