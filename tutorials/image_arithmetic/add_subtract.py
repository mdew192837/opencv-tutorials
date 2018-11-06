import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Create an array the same size as the image
# Values are 100
# Use the cv2.add() function to add 100 to each (no wrap)
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

# Create an array the same size as the image
# Values are 100
# Use the cv2.subtract() function to add 100 to each (no wrap)
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

# Wait for output
cv2.waitKey(0)