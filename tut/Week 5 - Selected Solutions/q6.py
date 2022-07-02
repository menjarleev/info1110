

def list_add(l1, l2):
	if len(l1) != len(l2):
		print("lists are of different sizes")
	sz = len(l1+l2)
	l = []
	for p in l1:
		l.append(p)
	for o in l2:
		l.append(o)
	return l
