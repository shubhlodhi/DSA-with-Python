# Write a program to reverse an array or string

def reverse(arr ,start,end):
    # for i in range(0,arr):
    if start >= end:
        return
    else:
        arr[start] , arr[end] = arr[end],arr[start]
        reverse(arr,start+1,end-1)
    

a = [12,13,14,15,16,18]
print(a)
(reverse(a,0,5))
print(a)

        
        
        


