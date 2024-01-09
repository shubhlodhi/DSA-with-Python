# a = [1,2,3,2,3,1]

def  repeat_find(a,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i] == a[j]:
                return a[i]


a = [10, 5, 3, 4, 3, 5, 6,10]
n = len(a)
print(repeat_find(a ,n))
# index = repeat_find(a,n)
# print(a[index])


# dict = { "shubh":{"lodhi":2},
        # "sslrp": 67,}

# print(dict["shubh"].keys())
# print(dict.values())

# second approach

def reaapiting(arr,a):
    find = -1
    mydict = dict()
    for i in range(n-1 ,-1,-1):
        if arr[i] in mydict:
            find = i 
        # else: append i value in the dict. 
            mydict[arr[i]] = 1


        print(find)
