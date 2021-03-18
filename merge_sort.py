import time


def merge(arr, l, m, r, drawdata, speed):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
        drawdata(arr)
        time.sleep(speed)
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        drawdata(arr)
        time.sleep(speed)
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            drawdata(arr)
            time.sleep(speed)

        else:
            arr[k] = R[j]
            j += 1
            drawdata(arr)
            time.sleep(speed)
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        drawdata(arr)
        time.sleep(speed)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        drawdata(arr)
        time.sleep(speed)


def merge_sort(arr, l, r, drawdata, speed):
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort(arr, l, m, drawdata, speed)
        merge_sort(arr, m + 1, r, drawdata, speed)
        merge(arr, l, m, r, drawdata, speed)
    drawdata(arr)
