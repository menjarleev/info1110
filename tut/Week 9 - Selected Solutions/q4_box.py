

class Box:
	def __init__(self, n):
		self.capacity = n
		self.items = []
		
	def add_item(self, item):
		if isinstance(item, Item):
			self.items.append(item)
			
	def weight(self):
		total_weight = 0
		for i in self.items:
			total_weight += i.get_weight()
			
		return total_weight
	
class Item:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		
	def get_weight(self):
		return self.weight
	
	def get_name(self):
		return self.name
		
b = Box(5) #Number of items it can hold
b.add_item(Item('Gameboy', 2))
b.add_item(Item('Book', 10))
b.add_item(Item('DVD', 1))
b.add_item(Item('Bluray', 1))
b.add_item(Item('Game1', 1))
b.add_item(Item('Game2', 1)) #Cannot fit
print("The box weighs: {}kg".format(b.weight()))
