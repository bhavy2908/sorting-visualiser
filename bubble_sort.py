import time
from main import stop


def bubble_sort(data, draw_data, speed):
    for n in range(len(data) - 1):
        check = 1
        store = len(data) - 1 - n
        for j in range(store):
            if data[j] > data[j + 1]:
                if stop:
                    return
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, optional_color='red', digit=j, end=store)
                time.sleep(speed)
                check = 2
                continue
            draw_data(data, optional_color='white', digit=j, end=store)
            time.sleep(speed)
        if check == 1:
            break
    draw_data(data)
