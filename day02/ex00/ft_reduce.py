def ft_reduce(function_to_apply, iterable):
	result = function_to_apply(iterable[0], iterable[1])
	for i in iterable[2:]:
		result = function_to_apply(result, i)
	return result

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print (ft_reduce(lambda u, v: u + v, lst))