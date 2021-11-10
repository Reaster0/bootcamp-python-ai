class Recipe:
	name = ''
	cooking_lvl = range(1, 5)
	cooking_time = 0
	ingredients = []
	description = ''
	recipe_type = ''

	def __init__(self, _name, _cook_lvl, _cook_time, _ingredients, _description, _recipe_type):
		if not _cook_lvl in range(1, 5):
			print("Error: cook_lvl =", _cook_lvl)
			raise ValueError
		if _cook_time < 0:
			print("Error: cook_time can't be negative")
			raise ValueError
		if not _recipe_type in {'starter', 'lunch', 'dessert'}:
			print("Error: the recipe type is unknown")
			raise ValueError
		if _name == '':
			print("Error: name can't be empty")
			raise ValueError
		if _ingredients == []:
			print("Error: ingredients can't be empty")
			raise ValueError
		
		self.name = _name
		self.cooking_lvl = _cook_lvl
		self.cooking_time = _cook_time
		self.ingredients = _ingredients
		self.description = _description
		self.recipe_type = _recipe_type
	
	def __str__(self):
		recipe = ["to make", str(self.name), "lvl:" , str(self.cooking_lvl), "you'll need", str(self.ingredients), "to make this", str(self.recipe_type), "it will take", str(self.cooking_time), "minutes," , "description:", str(self.description)]
		return ' '.join(recipe)
	
