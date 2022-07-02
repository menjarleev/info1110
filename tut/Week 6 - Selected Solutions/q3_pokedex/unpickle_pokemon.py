import pickle

types = ["N/A",
	"Grass",
	"Poison",
	"Fire",
	"Flying",
	"Water",
	"Steel",
	"Ground",
	"Bug",
	"Normal",
	"Electric",
	"Fighting",
	"Psychic",
	"Ice",
	"Ghost",
	"Rock",
	"Dragon",
	"Dark"]

f = open('pokemon.dex', 'rb')

pokemon = pickle.load(f)

for p in pokemon:
	print('{}'.format(p[6]))
	print('{}'.format(p[2]))
	print('{}'.format(p[3]))
	print('Level: {}'.format(p[0]))
	print('HP: {}'.format(p[4]))
	print('MAX_HP: {}'.format(p[5]))
	print()
