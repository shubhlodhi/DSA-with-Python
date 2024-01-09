def count_pair(arr,n ,k):
    count = 0
    for i in range(0,n):
        print("i",i , end=" ")
        
        for j in range(i+1,n):
            print("j" ,j,end=" ")
            if arr[i] + arr[j] == k:
                print("arr[i]",arr[i] ,"and" ,"arr[j]", arr[j] ,end=" ")
                print("\r")
                count+=1
    return count
        

a = [1, 5, 7, -1]

n = len(a)
print(count_pair(a,n,6))