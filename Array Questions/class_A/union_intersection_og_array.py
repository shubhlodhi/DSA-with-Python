# Given two sorted arrays, find their union and intersection.
# Example:

# Input: arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6} 
# Output: Union : {1, 2, 3, 4, 5, 6, 7} 
#          Intersection : {3, 5}

# Input: arr1[] = {2, 5, 6}
#         arr2[] = {4, 6, 8, 10} 
# Output: Union : {2, 4, 5, 6, 8, 10} 
#          Intersection : {6}


def union(arr1 ,arr2, n, m):
    i = 0
    j = 0
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            print(arr1[i] , end=" ")
            i+=1

        elif arr2[j] < arr1[i]:
            print(arr2[j] ,end=" ")
            j+=1

        else:
            print(arr2[j] , end=" ")
            i+=1
            j+=1

    while i<n:
        print(arr1[i] , end="")
        i+=1
    while j<m:
        # if j <= m:
            # print("no element")
        print(arr2[j], end=" ")
        j+=1

a = [1,2,3,4]
b = [4,5,6]
n = len(a)
m= len(b)
union(a,b,n,m)


        
        

    
    

