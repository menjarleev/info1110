import sys

n = int(sys.argv[1])

skip = 0
if len(sys.argv) > 2:
	skip = int(sys.argv[2])

i = 1
while i <= n:
	print('{} '.format(2*(i+skip)), end='') 
	i += 1
print()

