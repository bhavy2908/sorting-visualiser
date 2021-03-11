import time


def selection_sort(data, draw_data, speed):

    for i in range(len(data)):
        store = len(data) - 1 - i
        min_idx = i
        draw_data(data, optional_color='red', digit=i, end=store)
        time.sleep(speed)
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
                draw_data(data, optional_color='white', digit=j, end=store)
                time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
    draw_data(data)
