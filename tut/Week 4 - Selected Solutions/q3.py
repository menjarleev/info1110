import sys

eels = False
eel_count = 0


for s in sys.argv[1:]:
	if s == 'eels':
		eels = True
	elif s == 'eel':
		eel_count += 1
		

if eels:
	print("My hovercraft is full of eels")
elif eel_count > 0:
	print("There are " + str(eel_count) + " eels on my hovercraft")
else:
	print("There are no eels :(") 
	
