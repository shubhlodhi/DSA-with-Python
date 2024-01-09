import time
from check_if_sort import check_if_sort
# in sleep sorting you do pick the item according comparing the item to its time :
# if item is 24 then it genrate after 24 second and if item is 12 then it genrate after 12 seconds

def sleep_sort(arr):
    while not check_if_sort(arr):
        for i in range(len(arr)):
         time.sleep(arr[i])
         print(i)

a = [12,13,45,56]
sleep_sort(a)
        



