class ObjectC (object):
	def __init__ (self):
		pass

def doom_printer(obj):
	if obj is None:
		print ("ERROR: obj is None")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print ("end")

def what_are_the_vars(*args, **kwargs):
	result = ObjectC()
	i = 0
	for arg in args:
		setattr(result, 'var_' + str(i), arg)
		i += 1
	for arg in kwargs:
		setattr(result, arg, kwargs[arg])
	return result

obj = what_are_the_vars(7)
doom_printer(obj)
obj = what_are_the_vars("ft_lol", "Hi")
doom_printer(obj)
obj = what_are_the_vars()
doom_printer(obj)
obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
doom_printer(obj)
obj = what_are_the_vars(42, a=10, hello="world")
doom_printer(obj)