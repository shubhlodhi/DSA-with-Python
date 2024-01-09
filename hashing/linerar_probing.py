class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        
        self.next = None

class link_list:

    def __init__(self):
        self.head = None
        # self.n = 0
    # def __str__(self):
    #     return str(self.n)
    # traverse the link_list elements:

   


       
    def append(self , value,key): # we take the two argument self and value
        new_node = Node(value,key) # and in new_node define the Node class with value
        if self.head == None: # check if linked_list is empty
           self.head = new_node # then in head store the new_node
        #    self.n = self.n +1 # and increment the n with 1
        #    return # simply return to not execute the below code
        
        else:
           current = self.head # in cureent object store the haed value NONE
           while current.next != None: # lopp will run till current's next element will none.
            current = current.next #increment the value to 1
         # you are at the last node
           current.next = new_node # current 's next now store the new_node coz it is now in last node of link_list
        # self.n = self.n + 1 # increment to 1
   #  def print_data(self):
      #  while self.head != None:
         #  return self.head
   
       #clear functions:
    def clear(self): # clear takes one parameter self
       self.head = None # self.head is None
       self.n  = 0 # link_list nodes are 0
    def clear_head(self):
       if self.head == None:
          return "empty "
       else:
          self.head = self.head.next
   
   
    
    def delete_key(self ,key):
       if self.head.key == key:
          self.clear_head()
          return 
       if self.head == None:
          return "empty list"
       
       else:
        current = self.head
        while current.next != None:
          if current.next.key == key:
             break
          current = current.next
       if current.next == None:
          return "not found"
       else:
        current.next = current.next.next
    def search(self , key):
       current = self.head
       position = 0
       while current != None:
          if current.key == key:
            return position
          current = current.next
          position = position +  1
       return -1
   #  def traverse(self , index):
   #     current = self.head
   #     position = 0
   #     while current != None:
   #        if position == index:
   #           return str(current.key,"-->",current.value)
   #        current = current.next
   #        position = position + 1
    def size(self):
       temp = self.head
       counter  =0
       while temp != None:
          counter+=1
          temp = temp.next
       return counter
            
    def delete_index(self , index):
       current = self.head
       position = 0
       while current.next != None:
          if position == index:
             break
          current = current.next
          position = position +1
       current.next = current.next.next

    def traverse(self):
        current = self.head # cureent store the head(means a node which have data and address)
        result = '' # result is object with empty string
        while current != None: # when current is not equal to none loop will continue
         result = result + str(current.value)+"-->"+str(current.key) # + "-->" # till the loop condition become false 
         current = current.next  
        return result # [:-3]
    
    def get_node_at_index(self , index):# this function is use to take the index of linked_list.
       temp = self.head # here we used the temp to store the head value of link_list
       counter = 0 # counter is 0
       while temp is not None: # when temp is not none we start the loop
         if counter == index: # in every itertaion check if o=counter is equal to index
            return temp # return the value of index
         temp = temp.next # increment the temp
         counter += 1 # and counter
class dictionary:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        # create a LL araay
        self.buckets = self.make_array(self.capacity)
    # this function is to create the link_list in array now every index of array is now the link_list

    def make_array(self , capacity):
    #    l = [link_list()]*capacity
    # if we do this  method than same link list is create in the index of array
    # there address of link_list is same
      l = []     
      for i in range(capacity):
          l.append(link_list())
      return l
    
    
    def put(self,key,value): # Here we take two values one is key and value: 
       bucket_index = self.hash_function(key) # now we take the key hash value using of hash_function and store it in the bucket_index:
       node_index = self.get_node_index(bucket_index , key) # here we take the node index with the help of get_node_index.
      #  here we use the get_node_index function in thos function we take the bucket_index from the buckets_array in bucket index means the hash value of key
      # and check in the bucket_index search the key.
       if node_index == -1:
                #   insert 
        self.buckets[bucket_index].append(key,value)
        self.size += 1

        load_factor = (self.size/self.capacity)
        print(load_factor)

        if (load_factor) >= 2:
           self.rehash()

       else:
         # node = self.buckets[bucket_index].get_

        # upadte    
        node = self.buckets[bucket_index].get_node_at_index(node_index)
        node.value = value
    def rehash(self):
       self.capacity  =self.capacity *2
       old_buckets  = self.buckets
       self.size = 0
       self.buckets = self.make_array(self.capacity)

       for i in old_buckets:
          for j in range(i.size()):
            node = i.get_node_at_index(j)
            key_item = node.key
            value_item = node.value
            self.put(key_item,value_item)
    def get(self,key):
       bucket_index = self.hash_function(key)
       response  = self.buckets[bucket_index].search(key)
       if response == -1:
          return "Not Present"

       else:
          node = self.buckets[bucket_index].get_node_at_index(response)
          return node.value

    def __delitem__(self,key):
       buckets_index = self.hash_function(key)
       self.buckets[buckets_index].delete_key(key)
       self.size -= 1
    def __str__(self):
       for i in self.buckets:
          i.traverse()
       return ""
   
      

       
    def get_node_index(self,bucket_index , key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index
    def __setitem__(self,key,value):
       self.put(key,value)       
    def __getitem__(self , key):
       print(self.get(key))

    def hash_function(self,key):
       return abs(hash(key)) % self.capacity
   
          
        

    
d1 = dictionary(4)
# d1.buckets[2].traverse()
d1.put("python" , 34)
d1.put("ruby" , 23)
# d1.put("rub3y" , 23)
# d1.put("ruby2" , 23)
# d1.put("fff" , 34)
d1["shubh"] = 34
# d1["php"]  = 45
# d1["python"]
del d1["python"]
# d1["python"]
print(d1)