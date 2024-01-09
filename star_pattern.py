def star(n):
    for i in range(0, n):
        # for j in range(0 , i+1):
            # print(end=" *")
        for j in range(0,n+1):
            print(end=" ")   
            # n = n-1

        n = n-1
        for j in range(0 , i+1):
            print(end=" *")

            # j += 1
        print("\r")
    # n = i
    # k  = 0
        # for i in range(0,n):
        
        #  for j in range(0 , i ):
            # print(end=" *")
        #  n = n-1
print(star(6))