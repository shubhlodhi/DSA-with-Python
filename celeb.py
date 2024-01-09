from stack import Stack


L = [[0,0,1,0],
     [0,0,1,0],
     [0,0,0,0],
     [0,0,1,0]
    ]

def find_celeb(L):
    s = Stack()
    for i in range(len(L)):
        s.Push(i)
    while s.size() >= 2:

     i = s.pop()
     j = s.pop()
     if L[i][j] == 0:
       s.Push(i)
     else:
       s.Push(j)
    celeb = s.pop()
    # print(celeb)
    for i in range(len(L)):
       if i != celeb:
          if L[i][celeb] == 0 or L[celeb][i] == 1:
             print("no one is a celebrity")
             return
    print("the hero is" , celeb)

print(find_celeb(L))
             
       


