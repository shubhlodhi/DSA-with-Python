#  it is apply only on the sorted array:

def binary_search(arr,low,high,item):
    print (f"'low':{low} ,   'high'{high} " )
    if low<=high:  # take  parameter low and high chekc if low is higher than high than it is possible to sort
    #  for i in range(len(arr)):
        mid = low+high//2 # calculate the mid value
        print("mid",mid)
        if arr[mid] == item: # if mid of array is equal to item return mid
            # print("mid",mid)
            return mid
           
        elif arr[mid] >item: # if mid is greater than mid than decrement the mid and call function again (recursive)
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,high,mid+1,item)
    else:
       return "not found"
    

a = [10,20,30,40,50,60,70]
print(binary_search(a,0,len(a)-1 , 20))

# time_complexity is O(logn) , if you search k times then it is helpful


        