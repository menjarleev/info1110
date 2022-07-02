l = ['Jumpy', 'Jolly', 'Jolting', 'Jimmys']

for x in filter(lambda y: y.lower().startswith('jo'), l):
	print(x)
