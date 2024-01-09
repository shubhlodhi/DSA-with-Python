class Node:
    def __init__(self , value):
        self.data = value
        self.next = None
        

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    

    def is_empty(self):
       return(self.top == None)
    def Push(self,value):
        new_node  = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n = self.n +1
          
    def peek(self):
        if self.is_empty():
            print ("Stack is Empty")    
        else:
            print(f"top element - {self.top.data}")
    def pop(self):
        if self.is_empty():
            print( "STACK IS EPMTY")
        else:
            data = self.top.data
            self.top = self.top.next
            self.n = self.n -1
            return data
            # print(self.top)
        
            
    def traverse(self):
        current = self.top
        while current != None:
            print((current.data)) 
            current = current.next   
    # def __str__(self):
        # print(str(self.top))
    def size(self):
        return self.n
s = Stack()
# s.is_empty()
# (s.Push(2))
# (s.Push(1))
# (s.Push(3))
# (s.Push(5))

# # (s.peek)

# s.traverse()

# s.peek()
# s.pop()
# s.peek()
# s.pop()
# s.peek()
# s.pop()
# s.peek()
# s.pop()
# s.peek()
# s.pop()
# def reverse_string(value):
#     s = Stack()
#     for i in value:
#         s.Push(i)
#         print(i)
#     res = ""
#     while  not s.is_empty():
#         res = res + str(s.pop())
#     print(res)
# (reverse_string("Shubh"))


# def U_R(value,pattern):
#     r = Stack()
#     u = Stack()
#     for i in value:
#         data =u.Push(i)
#         print(data)
#     for i in pattern:
#         if i =="u":
#             data = u.pop()
#             r.Push(data)
#         else:
#             data = r.pop()
#             u.Push(data)
#     res = ""
#     while not u.is_empty():
#         res =   str(u.pop()) + res

#     print(res)       

# U_R("hello" , "uurr")
        
        
