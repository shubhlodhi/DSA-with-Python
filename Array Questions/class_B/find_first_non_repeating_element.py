def non_repeat(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and  arr[i] == arr[j]):
             
                break
            print("i-->",arr[i] ,"j-->" ,arr[j],i,j)
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1
    
# def again(arr,n):
#     for i in range(0,n):
#         for j in range(i+1,n):
#             # print(i , end=" ")
#             # print(j ,end=" ")
#             if a[i] == a[j]:
#                 # print(arr[j] , arr[i] )
#                 i+=1

#         return i

a = [1,2,3,1,2,4,5,6]
n = len(a)
print(non_repeat(a,n))
