
def list_to_string(l):
	s = ''
	if len(l) > 0:
		i = 0
		while i < len(l)-1:
			s += str(l[i]) + ', '
			i += 1
		s += str(l[i])
	
	return s


l = [1, 2, 3, 4, 5, 6]
s = list_to_string(l)
print(s)
