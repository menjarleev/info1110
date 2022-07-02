
def find_item(l, e):
	i = 0
	idx = -1
	while i < len(l):
		if l[i] == e:
			idx = i
			break
	
	
	return idx
	


l = [1, 2, 3, 4, 5, 6]

idx = find_item(l, 5)

if idx >= 0:
	print("Yes! I have found it at index {}".format(idx))
else:
	print('Unfortunately I have not found it')


