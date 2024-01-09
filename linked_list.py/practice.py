def fun(head):
    if head == None:
        return
    if head.next.next != None: # checks if head.next.next is not equal to None:
        print(head.data ,"", end="") # then it print the head
        fun(head.next) # calls again this function but now next element of function class 2
    print(head.data ,"" ,end="")# this execite when above recursion is completed.

