import time
def partition(data, start, end, draw_data, speed):
    pivot = data[start]
    low = start + 1
    high = end
    while True:
        while low <= high and data[high] >= pivot:

            high = high - 1
        while low <= high and data[low] <= pivot:
            time.sleep(speed)
            low = low + 1
            draw_data(data, optional_color='red', digit=low)
        if low <= high:
            time.sleep(speed)
            data[low], data[high] = data[high], data[low]
            draw_data(data, optional_color='white', digit=low, end = pivot)
        else:
            break
    data[start], data[high] = data[high], data[start]
    draw_data(data)
    return high
def quick_sort(data, start, end, draw_data, speed):
    if start >= end:
        return
    p = partition(data, start, end, draw_data, speed)
    quick_sort(data, start, p-1, draw_data, speed)
    quick_sort(data, p+1, end, draw_data, speed)