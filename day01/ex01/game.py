class GotCharacter:
	def __init__(self, first_name = 'default', is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	def __doc__(self):
		print("A personage that will probably die")

	def __init__(self, first_name='default', is_alive=True):
		super(Stark, self).__init__(first_name, is_alive)
		self.first_name = first_name
		self.is_alive = is_alive
		self.family_name = 'Stark'
		self.house_words = 'Winter is Coming'
	
	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		self.is_alive = False

	