import ctypes # this c type class hold the functionality of C.
# which we use in a python class.

# create a list:
class My_list:
  

    def __init__(self):
        # this is the initial size of array
        self.size = 1
        # trace the value size of array,elements present in array. 
        self.n = 0
        # an array which hold the make_arry function with size of array
        self.A = self.make_arry(self.size)

    def make_arry(self , capacity):
        # ctypes.py: create a c type array with refrential functioniltiy:
        return (capacity*ctypes.py_object)()
    # length functionlaity in class
    def __len__(self):
        return self.n
    # append/store functionality in class /algorithm
    def append(self , item):
        if self.size == self.n: # this condition says if size and n are equal then resize the array:
        # resize
         self.resize(self.size*2) # here we call a function of resize the array
        # append
        # we add the an item in array A on n.th position and increment the n value by 1 
        self.A[self.n] = item
        self.n = self.n +  1
    def resize(self , new_capacity): # create the new array called B
        # in B we add the new array function with new_capacity
        B = self.make_arry(new_capacity)
        # and the size of array is now a new_capacity
        self.size = new_capacity
        # now add the content of array A in array B:
        for i in range(self.n): # now start the range on n position and trace the elements of self.A(self.n) value.
            B[i] = self.A[i] # here in array B in i.th position we add self.A array  i.th value.
        self.A = B  # convert B array in a Array A. 
    # list syntax functionality:
    def __str__(self):
    #    [1,2,3] 
    # # to print the list create a list syntax like: [1,2,3] 
       result = ''
       for i in range(self.n):
           result = result +str(self.A[i]) + ","
       return '['+ result + ']'
    #  is to get the value of array according the index of array
    def __getitem__(self , index):
        # there is a get_item function which takes parameter as a index and self:
        if 0<= index < self.n:
        # here  condition if 0 is less than index and index is less than self.n than return the value of self.A array index.
          return self.A[index]
        else:
            return "index out of range"
    #  pop function is to delete the last elements of array
    def pop(self):
        # here pop function is pop the last value from the list
        if self.n == 0:
        # if list is empty then it return the value error
            return "value error"
        else:
        # here we print the n-1 value of array means last value of array will be deleted
         print(self.A[self.n-1])   
        # here we create the pop functionlity by decrement of value of array called n
         self.n = self.n - 1 
    #  clear function is clear the entire array
    def clear(self):
    #    this clear function is clear the entire array:
    #    so we define the size of array will be 1 and value of array will be 0
       self.size = 1
       self.n = 0
    # this function is to find the index of array by defining the value of array   
    def find_index(self , item):
        # in index function we trace the index of any array[element]
       for index in range(self.n): # here we trace the elements of self.n 
          if self.A[index] ==  item: # and here define the index of array self.A[index] is store the value of item 
           return index  # and return index of for loop
       return "value error"
    
    def insert(self , pos , item): # in insert function we pass two parameter position  to fetch the index of value and item to ftech the elements
       if self.size == self.n: # first check if array is full then
          self.resize(self.size*2) # resize the array

       for i in range(self.n , pos ,-1): # now we create a reverse loop to the position where we insert the item
          self.A[i] = self.A[i-1] # here store the value of i-1 in i position of an array , it is a shifting process 
        #   print(self.A[i])
        #   print(self.A[i-1])

       self.A[pos] = item  # when we find the postion in this position insert the item value
       self.n = self.n + 1 # and increment the value of n

    def __delitem__(self , pos): # in delete first we trace the position of delete item
     if 0 <= pos <self.n: # here checks if pos is in between the array n_size
       for i in range(pos , self.n-1): # run the loop from position to the n-1 position
          self.A[i]  = self.A[i+1] # insert the value of array i+1 in i positon of array ,shifting the array in right direction
       self.n =self.n-1 # and decrement the value of n

    def remove(self , posi): # in remove function first we take the position of a removed elements:
       pos = self.find_index(posi)# find the position , provide the index of the position


    #    delete
       if type(pos) == int: # check if element is integer or not
        pos = self.__delitem__(posi) # call delete_function its delete the find elements and shift the array from roght to left position
        return pos
       
       
          

      
    
L = My_list()
print(type(L))
print(len(L))
L.append("shubh")
L.append(20)
L.append(True)
# print(L)
# print(L[0],L[1])
# print(L.pop())
# print(L.pop())
# print(L)
# print(L.find_index(20))
# print(L.find_index("shubh"))
# s = [11,12,12]
# print(s[0])
print(L.insert(1 ,100))
# del (L[1])
print(L.remove(20))
print(L)
