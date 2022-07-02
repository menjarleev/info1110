

def mean(*args):
	s = 0
	# calculate the avg
	for a in args:
		s += a
	avg = s/len(args)

	max_diff = 0
	current = 0	
	#find the value furthest away
	for a in args:
		if abs(avg - a) > max_diff:
			max_diff = abs(avg - a)
			current = a
	
	return current
	

#Print and test
print(mean(1, 2, 3, 45, 80, 90, 90, 90))

