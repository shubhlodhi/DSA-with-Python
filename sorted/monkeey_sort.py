import random
from check_if_sort import check_if_sort
# monkey sort concept saysthat if you have some cards and cards sorted when the monkey is throw the card and collect it  then check if card
# is sort or not monkey do this process till card is not sorted>


#  so we use random module of python:
def monkey_sort(arr):
    while not check_if_sort(arr):
     random.shuffle(arr)
     print(arr)
    print(arr)
    # print(rand)
a = [12,12,45,34]
monkey_sort(a)
