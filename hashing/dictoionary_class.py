class dictionary:
    def __init__(self , size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,value):
        hash_value = self.hash_function(key)
    # first check in slot array index is none: if none then append
    # the key put in a slot index so key value is 1 according the hash function 
    # so it is define in the index 1 on array:  
    # and then in data_array on the hash_value(1) index[1] append the value(data) 
        if self.slot[hash_value] == None:
            self.slot[hash_value] = key
            self.data[hash_value] = value

        else:
        # if key is already available then:simply change the data_value not key_slot. 
            if self.slot[hash_value] == key:
        # it says if slot [hash value]_(1) and it is 
        # equal to the key () then simply change the data 
                self.data[hash_value] = value
            else:
                new_hash = self.rehash(hash_value) # hash value is now 2 means it is index 2 position
                while self.slot[new_hash] != None and self.slot[new_hash] !=  key:
                    new_hash = self.rehash(new_hash)
                if self.slot[new_hash] == None:
                    self.slot[new_hash] = key
                    self.data[new_hash] = value

                else: # if hash value of slot is equal to key then:
                    self.data[new_hash] = value



                    
        # in else condtition check slot hash value  is not same
        # as the key ttne we apply linear probbing in linear probbing we apply rehashing 
        # means calculate the rehash value again in rehash function we increment the value to 1.
    def get(self , key):
        # start my location according to the hash value:
        start_position = self.hash_function(key)
        # in current_position store the start position:
        current_position = start_position
        # run a awhile loop till current_position is not equal to none
        while self.slot[current_position] != None:
        # in between loop define a condition if self.slot[current_position] is equal to key which we serach
        # simplpy returns the the data of the position
            if self.slot[current_position] == key:
                return self.data[current_position]
        #  else: increment the positoin of cuurent_position by one using rehash function

            current_position = self.rehash(current_position) # increment the current position
        # also one condition obtain if current_position is equal to the startinng position:it
        # indicates that the value of key is not found and list is full
            if current_position == start_position:
                return "not found and also it is full"
        return "not found"
    def __getitem__(self , key):
        return self.get(key)
    def __setitem__(self , key ,value):
        return self.put(key,value)
    def __str__(self):
        for i in range(len(self.slot)):
            if self.slot[i] != None:
                print((self.slot[i]),":",(self.data[i]))
        return ""        
    def rehash(self , old_hash):
        return old_hash + 1


    def hash_function(self,key): # hash function is inbuilt function which
    # hash value is simply the integr value of any integer
    # if negative is value apperas we use abs() function
        return abs(hash(key)) %  self.size
        

s = dictionary(3)
# print(s.slot)
# print(s.data)
# s.put("python" , 45)
# s["python"]  = 1000
# if you want to update a value 
# s.put("python" , 1000)

s.put("java" , 23)
s.put("php" , 123)
# s["php"] = 37
print(s.get("php"))
print(s.get("python"))
print(s.slot)
print(s.data)
print((s))
# s['python'] = 100
# print(s.slot)

