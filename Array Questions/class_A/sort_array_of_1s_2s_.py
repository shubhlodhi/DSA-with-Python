# Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

# This problem is also the same as the famous “Dutch National Flag problem”

# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}

# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

def sort_array(arr , n):
    left = 0
    high = n-1
    mid =0
    while mid<=high:
        if arr[mid] == 0:
            arr[mid] , arr[left] = arr[left] , arr[mid]
            left+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1
    return arr
def show_arr(arr):
    for i in arr:
        print(i,end=" ")

arr = [ 0, 1, 2, 0, 1, 2]
# Output: {0, 0, 1, 1, 2, 2}
n= len(arr)
(sort_array(arr,n))
show_arr(arr)

