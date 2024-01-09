# problem if you have to unpack the N items but iterable maybe longer than the N items .
# so here we use star expressions

record = ["shubh" , "shubh.singh9411@g,ail.com" , 50 , 7456979356 , 9411911111]
# here we only unpack name and email address . so we apply start expressions in number section
#  this  condition obtain becoz if we have too many values to unpack and we only define the few varibales of few elements.so it throws error"
# ValueError: too many values to unpack (expected 4). if we write below line it throws this error. coz in the record list have 5 items but we only define the varibale only 4 items thats why we use this  
# start expressions
# name,e_mail,shares,phone_number = record
name,e_mail,shares,*phone_number = record
print(phone_number)


# here we iterating over the couples of tuple.

records = [
    ("boo" ,1,2),
    ("hash" , 2),
    ("boo" , 3,4),
]


# i ,y,k = records
i,*k , j  = records

# print(i)
print(j)

# def boo(x,y):
#     print("boo" , x,y)
# def hash(x):
#     print("hash",x)

# for i ,*y in records: # here we simply define the i to boo and *y to the rest values :1,2
#     if i == "boo":
#         boo(*y)
#         # print(*y)
#         print(i)
#     elif i == "hash":
#         hash(*y)

items = [1,2,3,4,5]
head,*tail = items
print(head)
print(tail)

    
