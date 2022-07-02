

players = []

players.append(input().split().reverse())
players.append(input().split().reverse())
players.append(input().split().reverse())

players.sort()

for p in players:
	print(p[1], p[0])



