import time
def count_sort(data, draw_data, speed):
	max_element = int(max(data))
	min_element = int(min(data))
	range_of_elements = max_element - min_element + 1
	count_data = [0 for _ in range(range_of_elements)]
	output_data = [0 for _ in range(len(data))]
	for i in range(0, len(data)):
		count_data[data[i]-min_element] += 1
	for i in range(1, len(count_data)):
		count_data[i] += count_data[i-1]
	for i in range(len(data)-1, -1, -1):
		output_data[count_data[data[i] - min_element] - 1] = data[i]
		count_data[data[i] - min_element] -= 1
	for i in range(0, len(data)):
		data[i] = output_data[i]
	draw_data(data)








