
import numpy as np
m , n = 4, 4       
def row_sum(arr) :
 
    sum = 0
 
    print("\nFinding Sum of each row:\n")
    for i in range(m) :
        for j in range(n) :
            sum += arr[i][j]
        print("Sum of the row",i,"=",sum)
        sum = 0

# Driver code    
if __name__ == "__main__" :
 
    arr = np.zeros((4, 4))
    x = 1  
    for i in range(m) :
        for j in range(n) :
            arr[i][j] = x
 
            x += 1
                 
    row_sum(arr)
 
