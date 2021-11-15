import numpy as np

class NymPyCreator(object):
	def from_list(self, lst):
		return np.array(lst)
	def from_tuple(self, tpl):
		return np.array(tpl)
	def from_iterable(self, itr):
		return np.array(itr)
	def from_shape(self, shape, values=0):
		return np.full(shape, values)
	def random(self, shape):
		return np.random.default_rng(0).random(shape)
	def identity(self, name):
		return (np.identity(name))