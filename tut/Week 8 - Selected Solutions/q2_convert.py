#n = 10
#l = []

#for i in range(10):
#	l.append(i)
#	
#for i, e in enumerate(l):
#	if e % 2 == 0:
#		l[i] = l[i] * 2

#print(l)

n = 10
l = []

i = 0
while i < 10:
	l.append(i)
	i += 1
	
i = 0
while i < len(l):
	if l[i] % 2 == 0:
		l[i] = l[i] * 2
	
print(l)
