# Given an array, the task is to cyclically rotate the array clockwise by one time. 

# Examples:  

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}

# Input: arr[] = {2, 3, 4, 5, 1}
# Output: {1, 2, 3, 4, 5}

def cyclic(arr , n):
    last_element = arr[n-1]
    for i in range(n-1 ,0,-1): # here minus 1 (-1) is used to make loop run from -1 position of index means loop run from right to
        #  left -1 represnts the last element of index
        arr[i] = arr[i-1]
    # print(arr)
        

    arr[0] = last_element

    return arr


a = [1,2,3,4,5]
n = len(a)
cyclic(a,n)
print(a)