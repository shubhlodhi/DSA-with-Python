#  in bubble sort we define pass every pass is completed when maximum number item in array is store in the last index of array
#  first we compare the item of array which are adjacent to each other, and chekc if item of array is larger than the adjacent item then it swap
#  the position


def bubble_Sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1-i):
         if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j] 
            flag = 1
        if flag == 0:
            break
    return arr


a  = [12,12,23,45,6,7,221,11]
print(bubble_Sort(a))

#  time_complexity = O(n) in best case scenario if the array is a;ready sortes if not then it takes O(N^2)
# it is adaptive in nature . means if array is alredy sorted then only one iteration or comparision occur in loop. with the help of flag
# it is stable means same value is occur in a sorted manner if in list[2,4,2,4] then first index 0 item is coming first then index 2 item . 