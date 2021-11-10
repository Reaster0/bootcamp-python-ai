class Vector:
	values = []

	def __init__(self, *values):
		if isinstance(values, int):
			for i in range(values):
				self.values.append(float(i))
			return
		if isinstance(values, range):
			for i in values:
				self.values.append(float(i))
		for i in values:
			self.values.append(i)
	
	def __mul__(self, other):
		result = []
		for i in self.values:
			for j in range(len(self.values[0])):
				result.append(i[j] * other)
		return result

	def __truediv__(self, other):
		result = []
		for i in self.values:
			for j in range(len(self.values[0])):
				result.append(i[j] / other)
		return result

lol = Vector([1.0, 2.0, 3.0])
#lol = Vector([1.0], [1.0], [3.0])
lol = lol * 2
print (lol)