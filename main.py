import numpy as np
import argparse
import cv2


def findCircle(image, par2, minR, maxR):
	width = 1008
	height = 756
	image = cv2.resize(image, (width, height))
	output = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	for y in range(height):
		for x in range(width):
			(h, s, v) = image[y, x]
			# check for basketball color
			if (h < 13 and s > 40 and s < 220 and v > 40 and v < 200) or (h > 200 and h < 250) or (s < 40 and v < 40):
				image[y, x] = (255, 255, 255)
			else:
				image[y, x] = (0, 0, 0)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cv2.imshow("output", gray)
	cv2.waitKey(0)

	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=par2, minRadius=minR, maxRadius=maxR)

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

		cv2.imshow("output", output)  # np.hstack([image, output]))
		cv2.waitKey(0)
	else:
		print("No circles found")


path = r'C:\Users\ColtonMulkey\Desktop\CodingProjects\Capstone\Validation\Left.jpg'
img = cv2.imread(path)
findCircle(img, 40, 110, 150)