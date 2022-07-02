

import sys

if len(sys.argv) == 2:
	val_out = int(sys.argv[1])
	print(val_out)
	
elif len(sys.argv) == 3:
	val_out = int(sys.argv[1])
	if (val_out < int(sys.argv[2]):
		val_out = int(sys.argv[2])
	print(val_out)
	
elif len(sys.argv):
	print("The problem to is too hard!")
