

config = {}
with open('q2_config.ini', 'r') as f:
	for l in f:
		if not l.startswith('#'):
			s = l.split()
			config[s[0]] = s[1]
			
print(config)
