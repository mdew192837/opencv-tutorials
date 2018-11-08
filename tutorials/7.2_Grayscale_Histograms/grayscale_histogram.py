from matplotlib import pyplot as plt
import argparse
import cv2
import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Resize the image - only because waves is huge
resized_image = imutils.resize(image, width=500)

# Convert to grayscale
image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Create the histogram
## Image - the list of images
## Channels - since we're grayscale, we're just doing [0], BGR would look like [0, 0, 0]
## Masks - we don't want any so we say None
## Bins - We want to see each pixel, so 256 bins per channel
## Range - We are RGB so we want 0 to 256
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot it using Matplotlib!
## Create a figure
## Label the Axes and give it title
## Set the xlim
## Show the plot
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)