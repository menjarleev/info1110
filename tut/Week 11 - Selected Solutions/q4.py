
def rec_fibonacci(n):
	if n <= 0:
		return 0
	elif n <= 1:
		return 1
	else:
		return rec_fibonacci(n-1) + rec_fibonacci(n-2)
		
print(rec_fibonacci(0))
print(rec_fibonacci(1))
print(rec_fibonacci(2))
print(rec_fibonacci(3))
print(rec_fibonacci(4))
print(rec_fibonacci(5))
		

