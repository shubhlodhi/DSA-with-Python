numRay = [1,2,2,1,3,4]
arr_size = len(numRay)
# print(arr_size , end=" ")
for i in range(0,arr_size):
    print("i" ,i,end=" ")
  
    x = numRay[i] % arr_size
    print("x" ,x , end=" ")
    numRay[x] = numRay[x] + arr_size
    print("arr" , numRay[x] , end=" ")
    print(numRay)

# time complex = O(n) space = O(1)
  
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " " , end=" "  )
# def find_dup(arr , n):
#     for i in range(0,n-1):
#         for  j in range(i+1,n):
#             if arr[i] == arr[j]:
#                 print(arr[i])


# a =[1,2,3,2,3]
# n = len(a)
# # print(n)
# # (find_dup(a,n))


# # but condition is here we find in the O(n) time and O(1) exttra space 

# print(0%6)
# print(0%9)
# def find(arr,n):
    # for i in range(0,n):





# print(-1+1)