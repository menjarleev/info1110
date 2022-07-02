
class TypedList:
	def __init__(self, type):
		self.item_type = type
		self.items = []
		
	def append(self, element):
		if isinstance(element, self.item_type):
			self.items.append(element)
			
	def prepend(self, element):
		if isinstance(element, self.item_type):
			self.items.insert(0, element)
	
	def insert(self, index, element):
		if isinstance(element, self.item_type):
			self.items.insert(index, element)
			
	def get(self,index):
		return self.items[index]
		
	def remove(self, index):
		del self.items[index]
		
	def __iter__(self):
		return TypedListIterator(self)
	
	#Extension
	def __getitem__(self, index):
		return self.get(index)
		
	def __len__(self):
		return len(self.items)
		
class TypedListIterator:
	
	def __init__(self, t_list):
		self.typed_list = t_list
		self.idx = 0
		
	def __next__(self):
		if self.idx < len(self.typed_list):
			value = self.typed_list.get(self.idx)
			self.idx += 1
			return value
		else:
			raise StopIteration
			
		
	
