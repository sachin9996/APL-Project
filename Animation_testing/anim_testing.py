import cv2

def image_path(i):
	return './images/'+str(i)+'.png'

def show_image(img):
	img = cv2.imread(img)
 	cv2.imshow('image',img)
 	cv2.waitKey(2000)

for i in range(1,3):
  show_image(image_path(i))

cv2.destroyAllWindows()