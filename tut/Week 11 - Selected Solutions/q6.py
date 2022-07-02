
def fibo_iterative(n):
	r = 0
	if n < 2:
		r = n
	else:
		i = 1
		s1 = 0
		s2 = 1
		while i < n:
			r = s1 + s2
			s1 = s2
			s2 = r
			i += 1
	
	return r
	
print(fibo_iterative(0))
print(fibo_iterative(1))
print(fibo_iterative(2))
print(fibo_iterative(3))
print(fibo_iterative(4))
print(fibo_iterative(5))
