import random

def generator(text, sep, option=None):
	assert isinstance(text, str) and isinstance(text, str) and isinstance(option , str) and option in ['shuffle', 'unique', 'ordered'], "the options are not supported"
	result = text.split(sep)

	if option == 'shuffle':
		result = random.sample(result, len(result))
	if option == 'ordered':
		result.sort()
	if option == 'unique': #WIP
		temp = []
		for item in result:
			if item not in temp:
				temp += [item]
		result = temp
	
	while result:	
		yield result[0]
		result.pop(0)

for i in generator("Le Lorem est Ipsum est simplement du faux faux texte.", " ", 'unique'):
	print (i)