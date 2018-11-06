import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# New image width of 150 pixels
# So we divide by the width (columns)
ratio = 150.0 / image.shape[1]
# This is the new image requirements
## Width of 150
## Once we have the ratio, we just multiply the rows (height)
dimensions = (150, int(image.shape[0] * ratio))

resized = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized)

resized = imutils.resize(image, width=1000)
cv2.imshow("Resized 9width", resized)

cv2.waitKey(0)