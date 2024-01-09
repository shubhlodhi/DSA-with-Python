class stackQ:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self , value):
       return self.s1.append(value)
    
    def pop(self):
        if  len(self.s2) == 0:
            while self.s1:
                (self.s2.append(self.s1.pop()))
        
            return self.s2.pop()
        return None
        
    def size(self):
        return self.s1 + self.s2
    def is_empty(self):
        return not self.s1 and self.s2
    
s = stackQ()
s.push(1)
s.push(2)
s.push(4)

s.pop()

print(s.size())  
s.pop()
print(s.size())
# print(s.is_empty()) 
