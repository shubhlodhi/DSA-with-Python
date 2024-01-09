# Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.

def sub_array(arr,n,x):
    count = 0
    for i in range(0,n):
        print("i",i,end="")
        current = arr[i]
        if current == x:
         return i
        else:
         for j in range(i,n):
          print("j",j,end="")
          count+=arr[j]
          print("count is total till range" ,count)
          print("arr add is" , arr[j])
          if count == x:
            # count+=i
           print(i,"to" , j)
        #    return
    print("not found")    
arr  = [ 0,5,5,10,67]
n = len(arr)
print(sub_array(arr,n,20)) 
print(arr)



# for i in range(5):
#   print("i",i)
#   for j in range(i+1):
    # print("j",j,end="")