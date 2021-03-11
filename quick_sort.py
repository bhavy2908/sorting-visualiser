import time


def partition(arr, low, high, draw_data, speed): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
        # If current element is smaller than or 
        # equal to pivot 
        draw_data(arr, digit=j, digit2=high, optional_color='white', var1=low, var2=high)
        if arr[j] <= pivot: 
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
            draw_data(arr, digit=j, digit2=i, optional_color='red', var1=low, var2=high)
        time.sleep(speed)
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1)


def quickSortA(arr, low, high, draw_data, speed): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high, draw_data, speed) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSortA(arr, low, pi-1, draw_data, speed) 
        quickSortA(arr, pi+1, high, draw_data, speed) 
        draw_data(arr)

def quick_sort(data, draw_data, speed):
    quickSortA(data, 0, len(data) - 1, draw_data, speed)