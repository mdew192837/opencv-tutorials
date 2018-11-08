import imutils
import cv2
import argparse
import numpy as np
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# Resize the image
image = imutils.resize(image, width=500)
# Convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Equalize the image
eq = cv2.equalizeHist(image)

# Show the image
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)