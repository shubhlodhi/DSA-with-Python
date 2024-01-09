# problem : you have an N element in tuple or any sequence unpack all the items in a sepreate varibales N.


sum = (12,13)
# so here store the elements of tuple sum in x and y varibales  
x,y = sum
print(x,y)

# another example:
data = ["shubh" , "shubh.singh9411@gmail.com" , 50 , (2021,12,21)]
# name , e_mail , shares_bought , date = data
# print(name , e_mail , shares_bought , date)

#  unpacking will work for any data if it is string or list , tuple etc.


s = "shubh"
h,g,j,k,p = s
print(h)
print(g)

#  in the time of unpacking you may sometimes discard some values:
data = ["shubh" , "shubh.singh9411@gmail.com" , 50 , (2021,12,21)]
# if we want to discard the email and share just simply write the _ in iteration of this elements.
name , _, shares_bought , _ = data
# print()