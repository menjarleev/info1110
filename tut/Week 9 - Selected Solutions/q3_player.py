

class Player:
	def __init__(self, name, score):
		self.name = name
		self.score = score
		
	def highscore(self):
		return self.score
		
	def highest_score(players):
		best_player = None
		if len(players) > 1:
			best_player = players[0]
			for p in players:
				if p.highscore() > best_player.highscore():
					best_player = p
					
		return best_player
				
player_list = [Player('Jim', 200), Player('James', 900), Player('Greg', 500), Player('Lisa', 700)] #Add other players and test your results
hp = Player.highest_score(player_list)
print("Highest Score: {} with {} points".format(hp.name, hp.score))
