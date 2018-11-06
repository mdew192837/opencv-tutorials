import argparse
import cv2
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# Grab the shape
(h, w) = image.shape[0:2]
# Calculate the center of the image
## Use half of the height and half of the width
center = (h // 2, w // 2)

# Pass in the center, angle, and scale of the image
M = cv2.getRotationMatrix2D(center, 45, 1.0)
# Output dimensions are in width and height
# We use (h, w) for the image because we say rows by columns, which is height by width
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# Pass in the center, angle, and scale of the image
M = cv2.getRotationMatrix2D(center, -90, 1.0)
# Output dimensions are in width and height
# We use (h, w) for the image because we say rows by columns, which is height by width
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)