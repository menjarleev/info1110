import sys

def substring(line, s):
	i = 0
	is_sub_str = False
	while i < len(line) and not is_sub_str and len(s) <= (len(line) - i):
		j = 0
		is_sub_str = True #We assume it is true
		while j < len(s) and is_sub_str:
			if s[j] != line[i+j]:
				is_sub_str = False
			j += 1
		i += 1
			
	return is_sub_str

if len(sys.argv) > 2:
	word = sys.argv[2]
	f = open(sys.argv[1], 'r')
	for idx, l in enumerate(f):
		if substring(l, word):
			print('{}. {}'.format(idx, l), end='')
