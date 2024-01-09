def merge_sort(arr ):
    if len(arr)  == 1:
        return 0
    
    divide = (len(arr)//2)
    left = arr[:divide]
    right  = arr[divide:]

    left = merge_sort(left )
    right = merge_sort(right)
    return sorted(left,right)

def sorted(arr1,arr2):
    i = j= 0
    merged = []
    while i < len(arr1) and j <len(arr2):
        if arr1[i] < arr2[j]:
         merged.append(arr1[i])
         i+=1
        else:
           merged.append(arr2[j])
           j+=1

    while i<len(arr1):
       merged.append(arr1[i])
       i+=1

    while j<len(arr2):
       merged.append(arr2[j])
       j+=1
    # for i in range(len(arr)):
        # if arr[i]

arr = [1,3,6,2,4,7,89]
n =len(arr)
print(merge_sort(arr ))
