import matplotlib.pyplot as plt
import matplotlib.image as img

class ImageProcessor:
	def load(self, path):
		try:	
			temp = img.imread(path)
			print("the image resolution is:", temp.shape[0], "x", temp.shape[1])
			return temp
		except:
			print("can't open the file")
	def display(self, array):
		plt.imshow(array)
		plt.show()