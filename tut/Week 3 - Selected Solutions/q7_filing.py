

import sys

v = 0
if len(sys.argv) > 1:
	with open(sys.argv[1], "r") as f:
		v = int(f.readline())
		if v % 2:
			v = (v * 3) + 1
		else:
			v = v / 2
			
	with open(sys.argv[1], "w") as f:
		f.write(str(v) + "\n")
else:
	print("Please specify a filename")
