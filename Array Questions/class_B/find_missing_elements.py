# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.

# Examples: 

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
# Output: 5
# Explanation: The missing number between 1 to 8 is 5
#  approach first:

# def missing(arr,n):
#     find = (n+1)*(n+2)//2
#     total = sum(arr)
#     return find - total


# a = [1,2,3,4,6]
# n = len(a)
# print(missing(a,n))

#  approach second:

# def missing(arr,n):
#     i ,total = 0 ,1
#     # print("i" , i,end=" ")
#     for i in range(2,n+2):
#         print("i new value is " , i , end=" ")
#         total+=i
#         print("total" , total ,end=" ")
#         total-=arr[i-2]
#         print("i value in here is" , i,end=" ")
#         print("negative_total" , total , end=" " )
#         print("\r")
#     return total

# a = [0,10,1,3,-20]
# n = len(a)
# print(missing(a,n))
# print(sum(a))

# def mssing1(a,n):
#     fond = False
#     maxi = max(a)
#     i =0
#     while i<maxi+1:
        
#         for j in range(i,n):
#             if a[j] == i:
            
#                 break
#         i+=1
#             # if a[j] == i:
#                 # break

#             # if a[j] == 0 :
#                 # break
    
        
#     return i

# a = [4,10,1,3]
# # a =[1,3,4,10]
# n = len(a)
# print(mssing1(a,n))
# print(max(a))
def mssing3(a,n):
    a1 = a.sort()
    # for i in range(1,n):
    i =1
    while i<n:
        if a[i-1] != i:
            # print(i)
            return i
        i+=1
        # print(i)
        # if a[i-1] == i:
        
    # return n+1
a = [1,2,3,4,5,7]
# a =[1,3,4,10]
n = len(a)
print(mssing3(a,n))
        
