def hailstone(n):
	l = [n]
	if n > 1:
		if n % 2:
			contents = hailstone((n*3)+1)
			l.extend(contents)
		else:
			contents = hailstone(n//2)
			l.extend(contents)
	return l
	
print(hailstone(5)) # [5, 16, 8, 4, 2, 1]

