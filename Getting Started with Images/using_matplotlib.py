import numpy as np
import cv2
from matplotlib import pyplot as plt

# load an image in grayscale (0): 1-Color; 0-Grayscale; -1-Un-change
img = cv2.imread('OpenCV_Logo.png', 0)

# display an image
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
