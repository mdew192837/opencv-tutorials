from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
import imutils


# This function just plots each channel given an image and the mask
def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])

# Boring Arguments Stuff
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

# Display the original image
image = cv2.imread(args["image"])
# Resize the image
image = imutils.resize(image, width=500)
cv2.imshow("Original", image)
# Plot the histogram for the original image
plot_histogram(image, "Histogram for Original Image")

# Create the mask
## Start by creating a numpy array of zeros
## Aka a black canvas
mask = np.zeros(image.shape[:2], dtype="uint8")
## Create a rectangle for the mask
## Filled in and is white
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
# Show the mask
cv2.imshow("Mask", mask)

# Use the mask and bitwise and to only get part of image we want
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)

# Plot the histogram with the mask
plot_histogram(image, "Histogram for Masked Image", mask = mask)

# Show both plots at the same time
plt.show()

cv2.waitKey(0)