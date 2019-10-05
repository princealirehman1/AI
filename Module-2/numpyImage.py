import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import numpy as np


myImageArray =pltimg.imread("afridi.jpg")

# image_array = np.asfarray(myImageArray[1:])

print("ndim: {0} shape: {1}".format(np.ndim(myImageArray),np.shape(myImageArray)))
myImageArray = myImageArray[:150,100:220,:]

afridi = plt.imshow(myImageArray)
print(afridi)
plt.show(afridi)


# print(myImageArray)