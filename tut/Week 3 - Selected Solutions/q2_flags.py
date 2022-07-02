
import sys

start = ''
end = ''
caps = False
word = ''

i = 1
while i < len(sys.argv):
	
	if sys.argv[i].startsWith("-f="):
		spl = sys.argv[i].split("=")
		if len(spl) > 1:
			front = spl[1]
		else:
			print("Invalid -f flag")	
	if sys.argv[i].startsWith("-e="):
		spl = sys.argv[i].split("=")
		if len(spl) > 1:
			end = spl[1]
		else:
			print("Invalid -e flag")
	if sys.argv[i] == "-caps":
		caps = True
	else:
		"""Treat the first word found as the only word to use"""
	 	word = sys.argv[i]

phrase = "{}{}{}".format(front, word, end)	 	
if caps:
	phrase = phrase.upper()
	
print("{}".format(phrase))
