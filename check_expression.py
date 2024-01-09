from stack import Stack


def expression(expreesion):
    s = Stack()
    # l_open = ["[" ,"{" ,"(" ]
    l_close = {"(":")" , "{":"}" , "[":"]"}
    for char in expreesion:
        if char in l_close.keys():
         s.Push(char)
        elif char in l_close.values():
           if  s.is_empty():
            return False
           top = s.pop()
           if l_close[top] != char:
             return False
              
           
    return True
        
print(expression("{(a+b)}"))


