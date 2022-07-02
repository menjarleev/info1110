
print("Please enter <player1> <player2> <scores>")
line = input()
line_spl = line.split()
p1 = line_spl[0]
p2 = line_spl[1]

g1 = line_spl[2].split("-")
g2 = line_spl[3].split("-")
g3 = line_spl[4].split("-")
g4 = line_spl[5].split("-")
g5 = line_spl[6].split("-")


p1_games = int(g1[0]) + int(g2[0]) + int(g3[0]) + int(g4[0]) + int(g5[0])
p2_games = int(g1[1]) + int(g2[1]) + int(g3[1]) + int(g4[1]) + int(g5[1])

p1_sets = int((int(g1[0]) >= 6))
p1_sets += int((int(g2[0]) >= 6))
p1_sets += int((int(g3[0]) >= 6))
p1_sets += int((int(g4[0]) >= 6))
p1_sets += int((int(g5[0]) >= 6))

p2_sets = int((int(g1[1]) >= 6))
p2_sets += int((int(g2[1]) >= 6))
p2_sets += int((int(g3[1]) >= 6))
p2_sets += int((int(g4[1]) >= 6))
p2_sets += int((int(g5[1]) >= 6))

print("{} won {} sets and {} games".format(p1, p1_sets, p1_games))
print("{} won {} sets and {} games".format(p2, p2_sets, p2_games))
