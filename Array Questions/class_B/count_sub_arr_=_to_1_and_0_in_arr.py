def count(arr ,n):
    mp = dict()
    sum = 0
    count = 0
    for i in range(0,n):
        if arr[i] == 0:
            arr[i] = -1
            print(arr[i] ,end=" ")
        sum += arr[i]
        if sum == 0:
            count+=1
        if (sum in mp.keys()):
            count+=mp[sum]
        mp[sum] = mp.get(sum,0)+1
    return count
    


arr = [1, 0, 0, 1, 0, 1, 1]
 
n = len(arr)
 
print("count =",
      count(arr, n))




k  = 2
n = 5
for i in range(0,n):
    if i == k:
        print("i" ,k ,i)
    if i!= k:
        print(k)


# mp ={}
    #   2: "lodhi"}


# a = mp.get(1,0)+1
# print(a)
# print(mp)
