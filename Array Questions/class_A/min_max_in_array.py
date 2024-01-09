# Given an array, write functions to find the minimum and maximum elements in it. 

# The most simplest way to find min and max value of an element is to use inbuilt function sort() in java. So, that value at 0th position will min and value at nth position will be max.

# explanation : there is many approach :

# first solution

# a = [12,13,56,15,16,27]
# a.sort()
# print(f"minumun value:{a[0]} , maximun value: {a[-1]}")


# # second solution:
# print(min(a))
# print(max(a))

# third solution:
def get_min(arr,n):
    if n ==1:
        return arr[0]
    # for i in range((n-1)):
        # min  = i
        # for j in range(0, i+1):
        #  if arr[j] < arr[j+1]:
    else:
        return(min(get_min(arr[1:] , n-1),arr[0]))   
         
            # min = i

        # return res
def get_max(arr,n):
        if n == 1:
            return arr[0]
        
        else:
               return max(get_max(arr[1:],n-1),arr[0])
arr = [12,23,4,56,432,12]
n = len(arr)

print(get_min(arr,n))

        