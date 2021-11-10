import datetime
from recipe import Recipe

class Book:
	name = ''
	last_updated = 0
	creation_date = 0
	recipes_list = {'starter' : [], 'lunch' : [], 'dessert' : []}

	def __init__(self, name):
		self.name = name
		self.creation_date = datetime.datetime.now()
		self.last_updated = datetime.datetime.now()
	
	def get_recipe_by_name(self, name):
		for i in range(len(self.recipes_list['starter'])):
			if self.recipes_list['starter'][i].name == name:
				print (self.recipes_list['starter'][i])
		for i in range(len(self.recipes_list['lunch'])):
			if self.recipes_list['lunch'][i].name == name:
				print (self.recipes_list['lunch'][i])
		for i in range(len(self.recipes_list['dessert'])):
			if self.recipes_list['dessert'][i].name == name:
				print (self.recipes_list['dessert'][i])
		raise ValueError

	def get_recipes_by_types(self, recipe_type):
		for i in self.recipes_list:
			if recipe_type == i:
				for j in range(len(self.recipes_list[i])):
					print (self.recipes_list[i][j].name)
				return
		print("the recipe type dosen't exist")
		raise ValueError

	def add_recipe(self, recipe):
		if not isinstance(recipe, Recipe):
			print("Invalid recipe type")
			raise ValueError
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_updated = datetime.datetime.now()
