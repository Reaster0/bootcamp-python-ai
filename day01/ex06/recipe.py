
cookbook = {'sandwich' : {'ingredient' : {'ham', 'bread', 'cheese', 'tomatoes'}, 'meal' : 'lunch', 'prep_time' : 60},
			'cake' : {'ingredient' : {'flour', 'sugar', 'egg'}, 'meal' : 'dessert', 'prep_time' : 60},
			'salad' : {'ingredient' : {'avocado', 'arugula', 'tomatoes', 'spinach'}, 'meal' : 'lunch', 'prep_time' : 15}}

def list_recipes(book):
	print("list of all recipes:")
	for recipe in book:
		print(recipe)

def print_recipe(book):
	recipe = input("Please input the name of the recipe to search for: ")
	if not book or not recipe in book:
		print("No book or recipe")
		return
	print("Recipe for ", recipe, ":")
	print("Ingredient list:", book[recipe]["ingredient"])
	print("it's best to eat for :", book[recipe]["meal"])
	print("and it take", book[recipe]["prep_time"], "DAYS to cook X-X")

def add_recipe(book):
	name_recipe = input("Insert the name of the recipe: ")
	ingredient = input("Put all the ingredients of the recipe: ")
	meal = input("What kind of meal is it?: ")
	prep_time = input("how much time does it take to bake?: ")
	book[name_recipe] = {'ingredient': ingredient, 'meal': meal, 'prep_time': prep_time}

def del_recipe(book):
	name_recipe = input("Put the name of the recipe to delete: ")
	if name_recipe in book:
		del book[name_recipe]
	else:
		print("This recipe dosent exist")

def interactive():
	print("\nselect an option with the number\n",
	"1: Add a recipe\n",
	"2: Delete a recipe\n",
	"3: Print a recipe\n",
	"4: Print the recipe list\n",
	"5: Quit this very bad program")
	answer = input("Insert your answer: ")
	if answer == '1':
		add_recipe(cookbook)
	elif answer == '2':
		del_recipe(cookbook)
	elif answer == '3':
		print_recipe(cookbook)
	elif answer == '4':
		list_recipes(cookbook)
	elif answer == '5':
		print("See you soon!")
		quit()
	else:
		print("Nope, invalid answer")
	interactive()


interactive()
