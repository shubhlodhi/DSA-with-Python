class stack:
    def __init__(self , value):
        self.size = value
        self.stack = [None] * self.size
        self.top = -1
        
    def push(self , value):
        if self.top == self.size - 1:
            return("Stack Over Flow")
       
        else:
         self.top = self.top + 1
         self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return "Empty Stack"
        data = self.stack[self.top]
        self.top = self.top - 1
        print(data)

        
    # def __str__(self):
        # if self.top == self.size:
        # current = self.top
        # while current != None:
            # return self.top
        #     return "Stack Overflow"
        # return str(self.stack)
    def Traverse(self):
        for i in range(self.top+1):
            print(self.stack[i], end=" ")

S = stack(3)

(S.push(4))
(S.push(3))
(S.push(6))
# (S.push(0))
# (S.pop())
# (S.pop())
# (S.pop())
(S.pop())
# S.Traverse()
(S.pop())
S.Traverse()
# S.Traverse()
# print(S)



        
