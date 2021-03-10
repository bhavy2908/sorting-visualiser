import time


def insertion_sort(data, draw_data, speed):
    for i in range(1, len(data)):
        store = len(data) - 1 - i
        key = data[i]
        j = i - 1
        draw_data(data, optional_color='red', digit=j, end=store)
        time.sleep(speed)
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, optional_color='white', digit=j, end=store)
            time.sleep(speed)
        data[j + 1] = key
    draw_data(data)






