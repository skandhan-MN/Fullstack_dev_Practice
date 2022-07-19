def smlNumThanCurr(nums):

    sortedArr = sorted(nums)
    dic = {}
    for i in range(len(sortedArr)):

        if sortedArr[i] not in dic:
            dic[sortedArr[i]] = i
            
    res = []
    
    for i in range(len(nums)):
        res.append(dic[nums[i]])
    
    return res


if __name__ == "__main__":

    nums = [8,1,2,2,3]
    ans = smlNumThanCurr(nums)
    print(ans)
