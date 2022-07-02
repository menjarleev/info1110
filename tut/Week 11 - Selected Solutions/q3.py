
def rec_factorial(n):
	if n <= 1:
		return 1
	else:
		return n * rec_factorial(n-1)
		
def binomial_coefficient(n, k):
	nf = rec_factorial(n)
	kf = rec_factorial(k)
	nkf = rec_factorial(n-k)
	
	return nf / (kf * nkf) 
	

