import time


def bubble_sort(data, draw_data, speed):
    for n in range(len(data) - 1):
        check = 1   # variable for checking if the array is already sorted
        store = len(data) - 1 - n
        for j in range(store):
            if data[j] > data[j + 1]:   # checking if the element found is greater than the previous one
                data[j], data[j + 1] = data[j + 1], data[j]  # swapping if a greater element is found
                draw_data(data, optional_color='red', digit=j, end=store)   # bar becomes 'red' if swapping occurs
                time.sleep(speed)
                check = 0   # if swapping is done check becomes '0'
                continue
            draw_data(data, optional_color='white', digit=j, end=store)     # bar becomes white if no swapping is done
            time.sleep(speed)
        if check == 1:  # if check is '1' this means no swap has happened
            break       # and the array is already sorted
    draw_data(data)
