from class_q import Queue

def fun(num):
    s = Queue()
    if num == 0:
        return 0
    else:
        s.En_Q(num%10)
        res = fun(num//10)
        res =  (s.De_Q() or 0) + res*10 
        return res
print(fun(523))
        
