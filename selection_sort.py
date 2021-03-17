import time


def selection_sort(data, draw_data, speed):
    for i in range(len(data)):  # traversing through the array
        min_idx = i
        draw_data(data, end=i-1, optional_color='white', digit=i)
        time.sleep(speed)
        for j in range(i + 1, len(data)):   # finding the smallest element in the unsorted array
            draw_data(data, end=i-1, optional_color='white', digit=j, digit2=i)     # bar stays white while searching
            if data[min_idx] > data[j]:
                min_idx = j
                draw_data(data, end=i-1, optional_color='red', digit=j, digit2=i)   # bar becomes red if a smaller
            time.sleep(speed)                                                       # element is found in the array
        data[i], data[min_idx] = data[min_idx], data[i]     # swapping the new smallest element
    draw_data(data, optional_color='cyan')                  # with the current smallest element
