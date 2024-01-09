def linear_search(arr , item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        else:
            return "not found"

a = [1,23,4,56]
print(linear_search(a,1))
#  linear search apply in the unsorted array as well as sorted array 
# time_complexity = O(n) in worst case scenario it is a brute force method:



