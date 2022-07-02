l = [1,4,5,2,3,3,7,54,2,1,9,8,8,6]

for x in filter(lambda y: y % 2 == 0, l):
	print(x)
