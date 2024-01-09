from class_q import Queue

def quee(value):
    q1 = Queue()
    q2 = Queue()
    for i in  ((value)):
        q1.En_Q(i)
        if q2.is_empty():
            
         q2.De_Q()
        # print(data2)
    res = ""
    while  not q2.top_front_pointer():
     res = (res) + (q2.De_Q())
     print(res)


g = [1,2,3,4] 
print(quee(g))



    
    