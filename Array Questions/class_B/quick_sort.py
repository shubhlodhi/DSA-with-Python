#  first approach:
# def quick_sort(arr):
#     n = len(arr)
#     if n<=0:
#         return arr
#     else:
#         pivot =  arr.pop()
#     # pivot = arr.pop()
#     left  = []
#     right = []
#     for i in arr:
#         if i > pivot:
#             right.append(i)
#         else:
#          left.append(i)

#     return quick_sort(left)+ [pivot] + quick_sort(right)



# a = [12,13,14,15,11]
# n = len(a)
# print(quick_sort(a))

# second approach: 

def partition(array, low, high ):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
    print("pivot" , pivot , end=" ")
 
    # Pointer for greater element
    i = low - 1
    print("i at present position" , i , end=" ")

 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            print("array j" ,array[j] , end=" ")
            print("pivot new position" , pivot , end=" ")
#  [1,2,4,56,8,53,7]
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            print("i new position" , i , end=" ")
      
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            print(array[i])
            print(array[j])
            print("\r")
    print("priviuos array" ,array)
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print("new array" , array)
    # Return the position from where partition is done
    print(i + 1)
    
# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

            
            
a = [1,2,4,56,8,53,7]
n = len(a)
print(partition(a,0,n-1))