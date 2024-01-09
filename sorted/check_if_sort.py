
def check_if_sort(arr): # check if array is sorted or not
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

a = [12,12,23,21,12]
print(check_if_sort(a))