def GoodPairs(nums):
    dic = {}
    count = 0
    for num in nums:

        if num not in dic:
            dic[num] = 1
        elif num in dic:
            count += dic[num]
            dic[num] += 1
            
    return count


if __name__ == "__main__":

    nums = [1,2,3,1,1,3]
    ans = GoodPairs(nums)
    print(ans)  