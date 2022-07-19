# Q-1 ) Select the appropriate code that performs selection sort.

# a)
"""
        for j in range(n):
            min = j
            for k in range(j+1,n):
                if(arr[k] < arr[min]):
                    min = k
            temp = arr[min]
            arr[min] = arr[j]
            arr[j] = temp
"""