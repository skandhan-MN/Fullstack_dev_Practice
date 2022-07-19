
def arrWaveForm(arr):
    arr.sort()
    for i in range(0, (len(arr) - 1), 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr



if __name__ == "__main__":
    arr = [10, 5, 6, 3, 2, 20, 100, 80]
    result = arrWaveForm(arr)
    print(arr)
	
