def selection_sort(arr):
    for i in range(len(arr)-1):
        min  = i
        # print("right now the minimun value is " , arr[i])
        for j in range(i+1 , (len(arr))):
            # print("the j value is " , arr[j])
            if arr[j] < arr[min]:
                min = j
                # print("now the min value is " , arr[min])
        arr[min],arr[i] = arr[i],arr[min]
    return arr

a = [12,23,34,54,22,12,11]
print(selection_sort(a))