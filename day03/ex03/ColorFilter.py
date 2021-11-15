import numpy as np
import sys
sys.path.insert(0, '../ex02')
sys.path.insert(0, '../ex01')
from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor

class ColorFilter:
	def invert(self, array):
		result = array.copy()
		result[:,:,0] = 255 - result[:,:, 0]
		result[:,:,1] = 255 - result[:,:, 1]
		result[:,:,2] = 255 - result[:,:, 2]
		# for i in result:
		# 	for r,g,b in i:
		# 		r = 255 - r
		# 		g = 255 - g
		# 		b = 255 - b
		return result
	def to_blue(self, array):
		result = array.copy()
		result[:,:,0] = np.zeros(result[:,:,0])
		result[:,:,1] = np.zeros(result[:,:,1])
		result[:,:,2] = result[:,:, 2]
	def to_green(self, array):
		pass
	def to_red(self, array):
		pass
	def to_celluloid(array):
		pass
	def to_grayscale(self, array):
		pass

scb = ScrapBooker()
cf = ColorFilter()
imp = ImageProcessor()
arr = imp.load('/Users/reaster/Pictures/large_earnaud.jpg')
#print (cf.to_blue(arr))
print (arr[0])
imp.display(cf.to_blue(arr))