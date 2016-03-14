"""
Custom Animation Library

"""

import cv2

window_name = "Tarjan's Algorithm - Strongly Connected Components"

# Defines the image path

def image_path(folder,i):
	return './'+folder+'/'+str(i)+'.png'

# Function which displays 'img' in a window named 'Tarjan's Algorithm - Strongly Connected Components' 
# and waits 'delay' seconds before moving on to load the next

def show_image(img,delay):
	img = cv2.imread(img)
	cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
 	cv2.imshow(window_name,img)
 	cv2.waitKey(int(delay))

# Displays the working of the algorithm sequentially at the given fps using opencv

def animate1(n,folder='Pictures',fps=1):
	for i in range(0,n):
  		show_image(image_path(folder,i),1.0*1000/(fps))
  	cv2.waitKey(0)
	cv2.destroyAllWindows()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
curr_image = 0

# Displays the working of the algorithm sequentially at the given fps using matplotlib

def animate2(n, fps=1):
	delay = 1.0/fps
	for i in range(n):
	    if i == 0:
	    	filename = './Pictures/' + str(i) + '.png'
	    	img = mpimg.imread(filename)
	    	show = plt.imshow(img) # Draws initial image
	        fig = plt.gcf()
	        plt.title("Tarjan's algorithm animation")
	    else:
	    	filename = './Pictures/' + str(i) + '.png'
	    	img = mpimg.imread(filename)
	    	show.set_data(img) # Update performed

	    plt.pause(delay)
	plt.pause(delay)

#Displays the images one at a time. Navigate through them using the arrow keys

def slideshow(n):
	filenames = ['./Pictures/' + str(i) + '.png' for i in range(n)]
	images = [mpimg.imread(f) for f in filenames]
	extent = (0, 1, 0, 1)
	pictures = [plt.imshow(images[i], extent=extent, aspect='auto') for i in range(n)]
	pictures[0] = plt.imshow(images[0], hold=True, extent=extent, aspect = 'auto')
	for i in range(1,n):
		pictures[i].set_visible(False)

	def toggle_images(event):
		global curr_image

		if event.key == 'right' or event.key == 'up':
			new_image = curr_image + 1
			new_image %= n
			pictures[new_image].set_visible(True)
			pictures[curr_image].set_visible(False)
			curr_image = new_image
			plt.draw()

		elif event.key == 'left' or event.key == 'down':
			new_image = curr_image - 1
			new_image %= n
			pictures[new_image].set_visible(True)
			pictures[curr_image].set_visible(False)
			curr_image = new_image
			plt.draw()
		else:
			return
		plt.draw()

	plt.connect('key_press_event', toggle_images)
	plt.show()
