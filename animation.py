"""
Custom Animation Library

"""

import cv2

# defines the image path

def image_path(folder,i):
	return './'+folder+'/'+str(i)+'.png'

# function which displays 'img' in a window named 'Tarjan's Algorithm - Strongly Connected Components' 
# and waits 'delay's before moving on to load the next

def show_image(img,delay):
	img = cv2.imread(img)
 	cv2.imshow("Tarjan's Algorithm - Strongly Connected Components",img)
 	cv2.waitKey(int(delay))

# Displays the working of the algorithm sequentially at the given fps

def start_animation(n,folder='Pictures',fps=1):
	for i in range(0,n):
  		show_image(image_path(folder,i),1.0*1000/(fps))
  	cv2.waitKey(0)
	cv2.destroyAllWindows()
