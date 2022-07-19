
def SortedArray(nums):
    n = len(nums)
    i = 0  
    j = n - 1
    k = n - 1
    result = list(range(n)) 

    while i <= j:
        SqrNg = nums[i] * nums[i]
        SqrPo = nums[j] * nums[j]
        if SqrNg < SqrPo:

            result[k] = SqrPo
            j = j - 1
        else:
    
            result[k] = SqrNg
            i = i + 1
        k = k - 1

    return result


if __name__ == "__main__":

    nums = [-4,-1,0,3,10]
    res = SortedArray(nums)
    print(res)




