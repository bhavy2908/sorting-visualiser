import time


def count_sort(arr, drawdata, speed):
    n = len(arr)
    arr1 = [0] * n
    x = [0] * (n + 1)
    for i in range(0, n):
        x[arr[i]] += 1
        drawdata(arr, optional_color='red', digit=i)
        time.sleep(speed)
    for i in range(1, n):
        x[i] += x[i - 1]
    i = n - 1
    while i >= 0:
        arr1[x[arr[i]] - 1] = arr[i]
        x[arr[i]] -= 1
        i -= 1
        drawdata(arr, optional_color='white', digit=i)
        time.sleep(speed)
    for i in range(0, n):
        arr[i] = arr1[i]
        drawdata(arr)
        time.sleep(speed)
