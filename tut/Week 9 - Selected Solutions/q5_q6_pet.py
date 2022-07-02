

class Pet:
	def __init__(self, name, age, species, house_trained):
		self.name = name
		self.age = age
		self.species = species
		self.house_trained = house_trained
		self.nicknames = []
		
	def add_nickname(self, nick):
		self.nicknames.append(nick)
		
	def has_nickname(self, nick):
		has_nick = False
		for n in self.nicknames:
			if nick == n:
				has_nick = True
				break
		
		return has_nick
		
		
