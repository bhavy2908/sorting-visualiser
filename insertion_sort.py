import time


def insertion_sort(data, draw_data, speed):
    for i in range(1, len(data)):   # traversing through the array
        key = data[i]
        j = i - 1
        draw_data(data, optional_color='white', end=i, digit=i)     # bar stays white when searching for smaller element
        time.sleep(speed)
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]   # moving the elements
            j -= 1
            draw_data(data, optional_color='red', end=i, digit=j, digit2=j + 1)     # becomes red if element is found
            time.sleep(speed)
        data[j + 1] = key
    draw_data(data)
