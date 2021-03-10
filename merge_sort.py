import time
def merge(data, l, m, r, draw_data, speed):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0 , n1):
		L[i] = data[l + i]
	for j in range(0 , n2):
		R[j] = data[m + 1 + j]
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			data[k] = L[i]
			i += 1
			time.sleep(speed)
		else:
			data[k] = R[j]
			j += 1
			time.sleep(speed)
		k += 1
	while i < n1:
		data[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		data[k] = R[j]
		j += 1
		k += 1
	draw_data(data)
def merge_sort(data,l,r, draw_data, speed):
	if l < r:
		m = (l+(r-1))//2
		merge_sort(data, l, m, draw_data, speed)
		merge_sort(data, m+1, r, draw_data, speed)
		merge(data, l, m, r, draw_data, speed)



