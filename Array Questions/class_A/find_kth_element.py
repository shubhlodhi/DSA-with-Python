s3 = [112,12,34,2,119]
s3.sort()
s1 = set(s3)
print(s1)

# print(s1)
if __name__ == '__main__':
    arr = [12, 3, 5, 7,12, 11,23]
    # N = len(arr)
    K = 4
 
    s = set(arr)
    print(s)
 
    for itr in s:
        print(itr)
        if K == 1:
            # print(K)
            print(itr)  # itr is the Kth element in the set
            break
        K -= 1

        # print(K)


