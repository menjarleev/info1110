
#Extension:
def a_range(start, end=None):
	if end == None:
		end = start
		start = 0
	
	while start < end:
		yield start
		start += 1
	

#Regular
def m_range(end):
	i = 0
	while i < end:
		yield i
		i += 1

print('m range')
for n in m_range(10):
	print(n)
	
print('a range with optional')
for n in a_range(2, 8):
	print(n)
	
print('a range without optional')
for n in a_range(8):
	print(n)
