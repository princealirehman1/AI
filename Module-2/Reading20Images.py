import matplotlib.pyplot as plt
import matplotlib.image as mimage
import numpy as np

class Reading20Images:

    def  __init__(self):
        self.imagesArray=np.array(2)
        pass

    def read20Images(self):
        for n in range(20):
            np.append(self.imagesArray,mimage.imread("images/{0}.jpg".format(n + 1)))
            # print("Looping : {0}".format(n + 1))
        print("ndim: {0} shape: {1}".format(np.ndim(self.imagesArray), np.shape(self.imagesArray)))

    def showImage(self,index):
        plt.imshow(self.imagesArray[index])

obj = Reading20Images()

obj.read20Images()

obj.showImage(0)

# NumPy Chapter 4 A1&A2 