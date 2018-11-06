import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

# Show the original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Flip the image
# 1 is horizontal (columns maybe)
# 0 is vertical (rows maybe)
# -1 is both
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Both", flipped)

cv2.waitKey()