from book import Book
from recipe import Recipe

master = Book("lol")
try:
	restRecipe2 = Recipe("pasta", 1, 1, 'italian boy', 'pasta made by italians', 'dessert')
	testRecipe = Recipe("cake", 3, 3, ["pasta", "rocks"], "this is a soup", 'dessert')
	master.add_recipe(testRecipe)
	master.add_recipe(restRecipe2)
except:
	quit()

try:
	master.get_recipes_by_types('dessert')
	master.get_recipe_by_name('pasta')
except:
	quit()

#print(str(testRecipe))
