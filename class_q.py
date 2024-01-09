class  Node:
    def __init__(self , value):
        self.data = value 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def En_Q(self ,value):
        new_node =  Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = self.front 
        else:
            self.rear.next = new_node
            self.rear = new_node

    def De_Q(self):
        if self.front == None:
            return None
        else:
            self.front = self.front.next


    def is_empty(self):
        return( self.front == None)

    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter  = counter +1
            temp = temp.next
        return counter
    def top_front_pointer(self):
        if self.front == None:
            return("Empty")
        else:
           return( self.front.data)
    def rear_pointer(self):
        if self.rear == None:
            return( "Empty")
        else:
            return(self.rear.data)
        

    def traverse(self):
        temp  = self.front
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

    


        
 
q = Queue()
q.En_Q(1) 
q.En_Q(4)
q.En_Q(6)
q.En_Q(3)# q.traverse() 
# q.De_Q()
# q.De_Q()
# q.traverse()
# q.is_empty()
q.top_front_pointer()
q.rear_pointer()
# q.rear_down_pointer()
# q.traverse()
# print("shubh")

