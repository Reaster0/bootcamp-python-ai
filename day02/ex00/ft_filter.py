def ft_filter(function_to_apply, iterable):
	result = []
	for item in iterable:
		if function_to_apply(item):
			result.append(item)
	return result

x = [1, 2, 3, 4, 5]
print (list(ft_filter(lambda dum: not (dum % 2), x)))