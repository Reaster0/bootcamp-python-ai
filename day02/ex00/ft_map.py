def ft_map(function_to_apply, iterable):
	result = []
	for item in iterable:
		result.append(function_to_apply(item))
	return result

def plus(iterable):
	iterable = iterable + 1

lol = [1, 2, 3, 4, 5]
ft_map(lambda x: x + 1, lol)
print (list(ft_map(lambda x: x + 1, lol)))