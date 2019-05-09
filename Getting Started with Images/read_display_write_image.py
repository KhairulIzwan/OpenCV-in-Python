import numpy as np
import cv2

# load an image in grayscale (0): 1-Color; 0-Grayscale; -1-Un-change
img = cv2.imread('OpenCV_Logo.png', 0)

#
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# or cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# display an image
cv2.imshow('image', img)

#First argument is a window name which is a string. second argument is our image. You can create as many windows as you wish, but with different window names.

# waits for specified milliseconds for any keyboard event
k = cv2.waitKey(0)
#If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.

if k == 27:
	# simply destroys all the windows created
	cv2.destroyAllWindows()
	#or cv2.destroyWindow('image')
elif k == ord('s'):
	# write an image
	cv2.imwrite('New_OpenCV_Logo.png', img)
	# First argument is the file name, second argument is the image
	cv2.destroyAllWindows()
