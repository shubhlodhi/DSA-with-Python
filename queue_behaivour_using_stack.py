from collections import deque
class stack:
    def __init__(self):
        # self.stack1 = []
        # self.stack2= []
        self.stack1 = deque()
        self.stack2 = deque()


    def push(self , value):
        self.stack1.append(value)
        while self.stack1:
         self.stack2.append(self.stack1.popleft())

    def pop(self):
        while  len(self.stack1):
         
            self.stack1.popleft()
    def top(self):
        if (self.stack1):
            return self.stack1[0]
        return None
 
    def size(self):
        return len(self.stack1)
            

        # if self.stack2:
        #    self.stack2.pop()
        # else:
        #    return None
    # def traverse(self):
    #    res = ""
    #    while len(self.stack2) != 0:
    #       res = str(self.stack2.pop()) + res
    #    print(res)
if __name__ == '__main__':       
 s = stack()
 s.push(1)
 s.push(2)
 s.push(3)
 print("current size: ", s.size())
 print(s.top())
 s.pop()
 print(s.top())
 s.pop()
 print(s.top())
 
 print("current size: ", s.size())
# s.traverse()
# from stack import Stack

# value = [1,2,3,4]
# def queue_behaviour(value):
#     s1 = deque()
#     s2 = deque()
#     for i in value:
#        s1.append(i)

#     #  print(data)
    
#     if len(s2 == 0):
#         if len(s1 == 0):
#            return "Empty"
#         data = s1.pop()
#         s2.append(data)
#     else:
#      s2.pop()

        
#         # if s1.is_empty():
#     #     return "queue is empty"
#     #  else:
#     #         data = s1.pop()
#     #         s2.Push(data)
            
#     # s2.pop()
#     # res = ''
#     # while not s2.is_empty():
#     #     res = str(s2.pop()) + res
#     # print(res)


# queue_behaviour("1234")

        
    
    # data = s1.pop()

    # s2.Push(data)
    # s2.pop()
