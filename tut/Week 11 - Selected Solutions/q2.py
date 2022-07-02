
def rec_factorial(n):
	if n <= 1:
		return 1
	else:
		return n * rec_factorial(n-1)

print(rec_factorial(2)) # 2
print(rec_factorial(3)) # 6
print(rec_factorial(4)) # 24


