import numpy as np
import argparse
import cv2


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

path = r'C:\Users\ColtM\Desktop\Coding Projects\TAMU\Validation\Shelf.jpg'
image = cv2.imread(path)
width = 1008
height = 756
image = cv2.resize(image, (width,height))
image = cv2.cvtcolor(image, cv2.COLOR_BGR2HSV)
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow("output", gray)
#cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
#(b, g, r) = image[0, 0]
#print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# access the pixel located at x=50, y=20
#(b, g, r) = image[20, 50]
#print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# update the pixel at (50, 20) and set it to red
#image[20, 50] = (0, 0, 255)
#(b, g, r) = image[20, 50]
#print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
for y in range(height):
	for x in range(width):
		(h,s,v) = image[y,x]
		#print(b,g,r)
		if r > 120 and g > 50 and g < 190 and b < 100:
			image[y,x] = (255,255,255)
		else:
			image[y,x] = (0,0,0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#output = gray
cv2.imshow("output", gray)
cv2.waitKey(0)


circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=120, maxRadius=150)

print("hello")
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output

	cv2.imshow("output", output) #np.hstack([image, output]))
	cv2.waitKey(0)
else:
	print("No circles found")