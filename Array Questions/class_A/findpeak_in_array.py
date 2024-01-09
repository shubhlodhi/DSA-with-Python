# Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.

# Note: If the array is increasing then just print the last element will be the maximum value.

# Example:

# Input: array[]= {5, 10, 20, 15}
# Output: 20


# Explanaition : there is simple explanation says if length of an array is 1 then there is no peak element exist. 
# check first element of an array: if arr[0] is greater than arr[1] then peak element is the first element
# check last element of an array: if arr[n-1] is greater than arr[n-2] then peak element is the last element.
# if both condotion are fail then check: rest elements: create a loop:
# for i in range(1,(n-1)): 
# in this loop check the ith element with i+1th element if ith element is gretaer then i+1th element and also ith element is gretaer then  
# i-1th element then print the ith element




# A Python3 program to find a peak element
 
# Find the peak element in the array
def findPeak(arr, n) :
 
    # first or last element is peak element
    # if (n == 1) :
    #   return 0
    # if (arr[0] >= arr[1]) :
    #     print("arr[0]:",arr[0])

    #     print("arr[1]:",arr[1])
    #     return 0
    # if (arr[n - 1] >= arr[n - 2]) :
    #     print("n-1:",arr[n-1])
    #     print("n-2:",arr[n-2])
    #     return n - 1
  
    # check for every other element
    for i in range(1, n -1):
  
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            # print(arr[i] ,arr[i+1] , arr[i-1])
         return(arr[i])
             
# Driver code.
# arr = [ 1, 3, 20, 4, 78, 0 ]
arr= [5, 10 , 27,25,78]
n = len(arr)
# print(n)
print("Index of a peak point is", findPeak(arr, n))
 
# This code is contributed by divyeshrabadiya07