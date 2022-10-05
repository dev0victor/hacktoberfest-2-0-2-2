def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
 
arr = list(map(int, input().split()))
 
arr_sort = bubbleSort(arr)
 
print("Sorted array is:", arr_sort)
