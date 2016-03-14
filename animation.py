"""
Custom Animation Library

"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
curr_image = 0

# Displays the working of the algorithm sequentially at the given fps using matplotlib

def animate(n, fps=1):
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
	images = [mpimg.imread(f) for f in filenames] # Getting the images
	ratio = len(images[0])*1.0/len(images[0][0])
	extent = (0, 1, 0, 1)
	pictures = [plt.imshow(images[i], extent = extent, aspect = ratio) for i in range(n)] #Draws all the pictures
	pictures[0] = plt.imshow(images[0], hold = 	True, extent = extent, aspect = ratio)
	for i in range(1,n):
		pictures[i].set_visible(False) # But all except one are not visible

	def toggle_images(event):
		global curr_image

		if event.key == 'right' or event.key == 'up': # Navigate to next image
			new_image = curr_image + 1
			new_image %= n
			pictures[new_image].set_visible(True)
			pictures[curr_image].set_visible(False)
			curr_image = new_image
			plt.draw()

		elif event.key == 'left' or event.key == 'down': # Navigate to previous image
			new_image = curr_image - 1
			new_image %= n
			pictures[new_image].set_visible(True)
			pictures[curr_image].set_visible(False)
			curr_image = new_image
			plt.draw()
		else:
			return
		plt.draw()

	plt.connect('key_press_event', toggle_images) # Binding to key press event
	plt.show() # Showing the drawing
