# Input: 
# ar1[] = {1, 5, 10, 20, 40, 80} 
# ar2[] = {6, 7, 20, 80, 100} 
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
# Output: 20, 80


def common(arr,arr1,arr2 , n,n1,n2):
    i,j,k = 0 ,0,0

    while (i<n and j<n1 and k<n2):
        if arr[i] == arr1[j] and arr1[j] == arr2[k]:
            print( arr[i])
            i+=1
            j+=1
            k+=1
        elif arr[i] < arr1[j]:
            i+=1
        elif arr1[j]< arr2[k]:
            j+=1

        else:
            k+=1


arr = [1, 5, 10, 20, 40, 80] 
arr1 = [6, 7, 20, 80, 100]
arr2 = [3, 4, 15, 20, 30, 70, 80, 120] 
n = len(arr)
n1 = len(arr1)
n2 = len(arr2)

print(common(arr,arr1,arr2 ,n,n1,n2))

    # n = len(arr)
    # n1 = len(arr1)
    # n2 = len(arr2)
    # n3  = []

    # for i in range(0,n):
    #     for j in range(0,n1):
    #         for k in range(0,n2):
    #             if arr[i] == arr1[j] and arr2[k]: 
                  
    #                 # if arr[i] == arr[k]:
                   
    #                 #   print(arr[j])
    #                 #   print(arr[k])
    #                 #   s = n3.append(arr[i])
    #                 print("arr" ,arr[i] , end=" ") 
    #                 #   print(arr[i], end=" ")
    #             print(arr1[j], end=" ")
    #             print(arr2[k], end=" ")
    #             print(arr[i] ,end=" ")
            
            # print(arr[i] ,"=" , arr1[j] , end=" ")
            
                
# arr = [1, 5, 10, 20, 40, 80] 
# arr1 = [6, 7, 20, 80, 100]
# arr2 = [3, 4, 15, 20, 30, 70, 80, 120] 

# print(common(arr,arr1,arr2))
                
            






