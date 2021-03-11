import time


def merge_sort(nlist, drawdata, speed):
	if len(nlist) > 1:
		mid = len(nlist) // 2
		lefthalf = nlist[:mid]
		righthalf = nlist[mid:]

		merge_sort(lefthalf, drawdata, speed)
		merge_sort(righthalf, drawdata, speed)
		i = j = k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				nlist[k] = lefthalf[i]
				i = i + 1
			else:
				nlist[k] = righthalf[j]
				j = j + 1
			k = k + 1
			drawdata(nlist, optional_color='red', digit=i)
			time.sleep(speed)

		while i < len(lefthalf):
			nlist[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		while j < len(righthalf):
			nlist[k] = righthalf[j]
			j = j + 1
			k = k + 1
		drawdata(nlist, optional_color='white', digit=i)
		time.sleep(speed)
	drawdata(nlist)
