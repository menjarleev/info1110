l = ['Sample', 'sambo', 'sound', 'sniffle', 'snore']

l.sort(key=lambda x: x.lower())
for x in l:
	print(x)
