
def intersection(nums1, nums2):
    
    uniqueList = []
    nums1 = sorted(set(nums1))
    nums2 = sorted(set(nums2))
    
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            uniqueList.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]: 
            j += 1
        else: 
            i += 1
            
    return uniqueList


if __name__ == "__main__" :

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    ans = intersection(nums1, nums2)
    print(ans)




