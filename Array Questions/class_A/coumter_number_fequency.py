# first approach : time complexity = O(n)
# def count(arr,k):
#     n = 0
#     for i in range (len(arr)):
#         if arr[i] == k:
#             n+=1
#     return n
#      Using recursive approach: help of binary search
def binary_serach(arr,l,r,x):
    if l>r:
        return -1
    
    mid = (l+r)//2

    if arr[mid] == x:
        return mid
    if arr[mid]>x:
        return binary_serach(arr,l,mid-1,x)
    return binary_serach(arr,mid+1,r,x)

#  now create the function which help us to count the serach value

def count(arr,n,x):
    ind = binary_serach(arr,0,n-1,x)



    if ind == -1:
        return 0
    count = 1
    # check from the left position
    left = ind-1
    while left >= 0 and arr[left]== x:
        count+=1
        left-=1
    # check from the right position
    right = ind+1
    while right < n and arr[right] == x:
        count+=1
        right+=1

    return count








arr = [1,1,2,2,2,3,3,4,4,4,4]
n= len(arr)
print(count(arr,n,2))