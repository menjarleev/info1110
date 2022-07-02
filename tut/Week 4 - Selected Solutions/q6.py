

def rotn(str_1, n):
	rot_str = ''
	for s in str_1:
		o = (ord(s))
		if o >= 97 and o <= 122:
			rot_str += chr((((o - 97) + n) % 26) + 97)
		elif o >= 65 and o <= 90:
			rot_str += chr((((o - 65) + n) % 26) + 65)
		elif o >= 48 and o <= 57:
			rot_str += chr((((o - 48) + n) % 10) + 48)
		
	return rot_str
		

