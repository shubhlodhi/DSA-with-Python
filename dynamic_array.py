# create list [D]
import sys
l= []
d = sys.getsizeof(l)
print(d)
for i in range(100):
     print(i , sys.getsizeof(l) )
         
     l.append("shubh")

print(d)

d = sys.getsizeof(l)
print(d)

# list behave like a dynamic array it adjudt its
# acording to its input.


