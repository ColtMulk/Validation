import numpy as np
import cv2

from GravityPhysics import *


def findCircle(image, par2, minR, maxR):
    width = 1008
    height = 756
    image = cv2.resize(image, (width, height))
    output = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    avg = 0
    count = 0
    for y in range(height):
        for x in range(width):
            (h, s, v) = image[y, x]
            # check for basketball color
            if (h < 10 and s > 40 and s < 220 and v > 40 and v < 200):  # or (s < 40 and v < 40):
                image[y, x] = (255, 255, 255)
                avg += y
                count += 1
            else:
                image[y, x] = (0, 0, 0)
    avg /= count
    print("Image Average: " + str(avg))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("output", gray)
    cv2.waitKey(0)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=par2, minRadius=minR, maxRadius=maxR)

    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        count = 0
        avg = 0
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            count += 1
            avg += y
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        # show the output
        avg /= count
        print(avg)
        cv2.imshow("output", output)  # np.hstack([image, output]))
        cv2.waitKey(0)
    else:
        print("No circles found")





path = r'C:\Users\ColtM\Desktop\Coding Projects\TAMU\Validation\BasketballMid.jpg'
img = cv2.imread(path)
#findCircle(img, 20, 40, 60)

print(timeDiff(5, 20))
print(timeDiff(0.1, 0.25))

d = getTime(0.1)

print(nextFallPoint(5, 1))
print(nextFallPoint(d, 1))
