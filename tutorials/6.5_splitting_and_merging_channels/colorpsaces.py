import cv2
import numpy as np
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# When we got a large image, we just be using imutils
resized_image = imutils.resize(image, width=500)
cv2.imshow("Original", resized_image)
# cv2.imshow("Original", image)

# Convert the image to grayscale
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Convert the image to HSV
hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Convert the image to L*A*B
lab = cv2.cvtColor(resized_image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*A*B", lab)

cv2.waitKey(0)