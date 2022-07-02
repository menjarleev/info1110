

t = tuple()
p = list()

with open('q1_file.txt', 'r') as f:
	for l in f:
		t += (l,)

for i in t:
	p.append(i)
	
print(t)
print(p)
