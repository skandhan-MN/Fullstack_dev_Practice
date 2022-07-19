def merge(nums1, m, nums2, n):

	last = m + n - 1
	i, j = m - 1, n -1
    
	while last >= 0:
		if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
			nums1[last] = nums1[i]
			i -= 1
		else:
			nums1[last] = nums2[j]
			j -= 1
		last -= 1
	return nums1


if __name__ == "__main__" :

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    ans = merge(nums1, m, nums2, n)
    print(ans)




