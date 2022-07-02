

def factorial(n):
	r = 1
	if n > 0:	
		j = 1
		
		while j <= n:
			j += 1
			yield r
			r = r*j
	else:
		yield r
		
for f in factorial(4):
	print(f)


