import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):
		return array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]] #check the error when it goes past the array len
	
	def thin(self, array, n, axis):
		if axis:
			return np.delete(array, slice(n -1, None, n), axis) #make all of the check error
		return np.delete(array, slice(n -1, None, n), 0)

	def juxtapose(self, array, n, axis):
		result = array.copy()
		if axis:
			for i in range(n - 1):
				result = np.concatenate((result, array), axis)
			return result
		for i in range(n - 1):
			result = np.concatenate((result, array), 0)
		return result
		
	def mosaic(self, array, dim):
		result = array.copy()
		for i in range(dim[0] - 1):
			result = np.concatenate((result, array), 0)
		for i in range(dim[1] - 1):
		 	result = np.concatenate((result, result), 1)
		return result

