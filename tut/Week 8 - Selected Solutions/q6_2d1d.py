import random

# my N * M 2d matrix
N = 5
M = 10

matr = [0]*(M*N)

i = 0

#Displaying a random matrix
while i < N:
	j = 0
	while j < M:
		matr[(i * M) + j] = random.randint(0, 9)
		print('{}'.format(matr[(i * M) + j]), end='')
		j += 1
	print('')
	i += 1
