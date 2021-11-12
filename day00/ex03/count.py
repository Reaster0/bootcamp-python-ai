import string

def text_analyzer(*text):
	'''this function analyze a text and i find the concept of docstring very cool'''
	
	if not text:
		text = input("please input a string: ")
	if text[1:]:
		print("there is too much parameters")
		quit()
	if text == "":
		text = 0
		print("there is no characters in this string")
		quit()

	up_letters = 0
	low_letters = 0
	points = 0
	spaces = 0
	nbr_char = 0
	
	for i in text:
		if i.isspace():
			spaces += 1
		elif i.isalpha() and i.isupper():
			up_letters += 1
		elif i.isalpha() and i.islower():
			low_letters += 1
		elif i in string.punctuation:
			points += 1
		nbr_char += 1
	
	print("The text contains", nbr_char, "characters:\n",
	"-", up_letters, "upper letters\n",
	"-", low_letters, "lower letters\n",
	"-", points, "punctuation mark\n",
	"-", spaces, "spaces\n")