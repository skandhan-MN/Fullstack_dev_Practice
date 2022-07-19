
# Q-4 )[BONUS QUESTION] Write a while loop implementation of selection
# sort? (5 marks)

def selection_sort(A):
   
    n = len(A)
    i = 0
    while (i < (n -1)) :
        min_ele = A[i]
        min_ele_idx = i
        j = i
        while ((j+1) < n ):
            j += 1
            if A[j] < min_ele:
                min_ele = A[j]
                min_ele_idx = j
        A[i], A[min_ele_idx] = A[min_ele_idx], A[i]

        i += 1

    return A


if __name__ == "__main__":

    A = [6, 7, 1, 2, 4, 5, 6]
    print(selection_sort(A))


"""  
    Time Complexity =O(N^2)
    Space Complexity =O(1)
     
"""