
def findSubsetArr(arr1, arr2):
    count = 0
    temp = False
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                count = count + 1
            if count == len(arr2):
                temp = True
    if temp == True:
        print("arr2[] is subset of arr1[]")
    else:
        print("arr2[] is not a subset of arr1[]")



if __name__ == "__main__":
	
	# arr1 = [11, 1, 13, 21, 3, 7]
	# arr2 = [11, 3, 7, 1]

	arr1 = [10, 5, 2, 23, 19]
	arr2 = [19, 5, 3]

	findSubsetArr(arr1, arr2)




