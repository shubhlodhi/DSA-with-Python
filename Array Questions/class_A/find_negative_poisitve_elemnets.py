# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear 
# before all positive numbers.

# Examples : 

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5



# a = [1,2,34,-2,-3,-12,-4] 
# a.sort()
# print(a)

# def neg_pos(arr ,n):
#     # current = arr[0]
#     for i in range (0,n):
#         current = arr[i]
#         # if current == arr[i]:
#             # i+=1
            
#         for j in range(i+1 , n):
#             if arr[j] >= current:
#                 current, arr[j] = arr[j] , current 

#         print(arr)
        
def rearrange(arr, n ) :
 
    # Please refer partition() in
    # below post
    # https://www.geeksforgeeks.org / quick-sort / j = 0
    j = 0
    for i in range(0, n) :
        print("value of i" ,i , end="")
        if (arr[i] < 0) :
            print("value of arr[i]" , arr[i],end="")
            temp = arr[i]
            print("in temporray varibale store" ,temp,end="")
            arr[i] = arr[j]
            print("in array 0 position"  , arr[i])
            arr[j]= temp
            j = j + 1
        print(arr)
 

arr = [-1, -3, 1, 5, 2,-7,8 ]
n = len(arr)
rearrange(arr, n)
# a= [-2,-11,-5,2,1]
# n = len(a)
# neg_pos(a,n)


