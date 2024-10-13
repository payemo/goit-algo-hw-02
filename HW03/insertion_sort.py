def insertion_sort(arr):
    for i in range(1, len(arr)):
        v = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > v):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v