class Node:

    def __init__(self , value):
        self.data = value
        self.n = 0
        self.next = None


    def __str__(self):
        return str(self.n) 
class link_list:

    def __init__(self):
        self.head = None
        self.n = 0
    # def __str__(self):
    #     return str(self.n)
    # traverse the link_list elements:
    def __str__(self):
        current = self.head # cureent store the head(means a node which have data and address)
        result = '' # result is object with empty string
        while current != None: # when current is not equal to none loop will continue
         result = result + str(current.data)  # + "-->" # till the loop condition become false 
         current = current.next  
        return result # [:-3]
    def insert_head(self , value):
        new_node  = Node(value) # new node have class value
        new_node.next = self.head # new_node ka next is now self.head
        self.head = new_node # self.head have now value of new_node and now it have address and data are both available
        self.n = self.n + 1 # self.n is incrment to 1


       
    def append(self , value): # we take the two argument self and value
        new_node = Node(value) # and in new_node define the Node class with value
        if self.head == None: # check if linked_list is empty
           self.head = new_node # then in head store the new_node
           self.n = self.n +1 # and increment the n with 1
           return # simply return to not execute the below code
        
        current = self.head # in cureent object store the haed value NONE
        while current.next != None: # lopp will run till current's next element will none.
          current = current.next #increment the value to 1
        # you are at the last node
        current.next = new_node # current 's next now store the new_node coz it is now in last node of link_list
        self.n = self.n + 1 # increment to 1
   #  def print_data(self):
      #  while self.head != None:
         #  return self.head
    def insert_middle(self , value, after): # in middle function pass three paramter called self , value , after.
       new_node = Node(value) # here new_node stores the class node with value.
       current = self.head # here Current object stores the self.head (none value , and data)
       while current != None: # till current is not equal to none.
          if current.data == after: # here checks the condition if data of current (here current store the address and value)
           break # if upper condition is true then loop will break
          current = current.next # if not then current is increment to 1 means 
    #    print(current.data) # print where the node loop will end
       if current != None: # check if current is not equal to none (but now current object hold the object which have 3 value)
          new_node.next = current.next # here it says new_node ka jo next h wo current ka next h
          current.next = new_node # current.next is now a new node
       else: 
          return "out of range"
       #clear functions:
    def clear(self): # clear takes one parameter self
       self.head = None # self.head is None
       self.n  = 0 # link_list nodes are 0
    def clear_head(self): # clear_head takes one parameter self
       if self.head == None: # if head is none 
          return "empty list" # then simply returns empty list

       self.head = self.head.next # if not then head is now head's next node
       self.n = self.n - 1 # and decrement to 1
    # pop delete the last element:
    def pop(self): #pop takes only one paramter self
       if self.head == None: # check in head is equal to none
          return "empty LL" # if yes then return smpty LL
       current = self.head # if not then current object holds the self.head value(none).
       if current.next == None: # check if current ka next is equal to none
        return self.clear_head() # then simply calls clear_head function
       while current.next.next != None: 
          current = current.next
       current.next = None
       self.n = self.n - 1
    
    def delete_middle(self ,value):
       if self.head == None:
          return "empty LL" 
       if self.head.data == value:
          return self.clear_head()
       current = self.head
       while current.next != None:
          if current.next.data == value:
             break
          current = current.next
       if current.next == None:
          return "not found"
       else:
        current.next = current.next.next
    def search(self , item):
       current = self.head
       position = 0
       while current != None:
          if current.data == item:
            return position
          current = current.next
          position = position +  1
       return "EMPTY LIST"
    def __getitem__(self , index):
       current = self.head
       position = 0
       while current != None:
          if position == index:
             return current.data
          current = current.next
          position = position + 1
            
    def delete_index(self , index):
       current = self.head
       position = 0
       while current.next != None:
          if position == index:
             break
          current = current.next
          position = position +1
       current.next = current.next.next
   #  def fun(self):
   #    current = self.head
   #    if current == None:
   #       return
   #    if current.next.next != None:
   #       print(current.data,"",end="")
   #       fun(self)
   #    print(current.data ,"" ,end="")
    def replace_max(self , value):
      temp = self.head
      max = temp
      while temp != None:
         if temp.data > max.data:
            max = temp
         temp = temp.next
      max.data = value
    def sum_odd(self):
       temp = self.head
       pos = 0
       result = 0
       while temp != None:
          if pos%2 !=0:
             result = result + temp.data
          temp = temp.next
          pos  = pos +1
       return(result)
    def change_input(self):
       current = self.head
       while current != None:
          if current.data == "*" or current.data == "/":
             current.data = " "
             if current.next.data == "*" or current.next.data == "/":
                current.next.next.data = current.next.next.data.upper()
                current.next = current.next.next
          current = current.next


l = link_list()
# (l.append(2))
(l.insert_head(1))
(l.insert_head(2))
(l.insert_head(2))
(l.insert_head(3))
# print(l)
# l.traverse()
# l.append(2)
# print(l)
l.insert_middle(12,3)
# l.clear()
# l.pop()


# l.delete_middle(12)
# l.delete_middle(3)
# print(l)
# print(l.search(12))
print(l)
print(l.sum_odd())

# print(l)
# print(l[1])
# (l.delete_index(0))
# (l.replace_max(14))
# print(l)
# l.clear_head()
 
# print(l)
l.append("I")
l.append("*")
l.append("a")
l.append("m")
l.append("*")
l.append("/")
l.append("s")
l.append("h")
l.append("u")
l.append("b")
l.append("h")
l.append("*")
l.append("/")
l.append("l")
l.append("o")
l.append("d")
l.append("h")
l.append("i")

# print(l.print_data())
l.change_input()
print(l)