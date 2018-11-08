from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
cv2.imshow("Original", image)

cv2.waitKey(0)

# Split the channels
channels = cv2.split(image)
colors = ("b", "g", "r")

# Set up the plots
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

print(zip(channels, colors))

for (channel, color) in zip(channels, colors):
    # Calculate a new histogram for each channel
    # So the image in one channel, grayscale, 256 bins, all pixels
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    # Plot the hist, display the color
    plt.plot(hist, color = color)
    # Set the xlim
    plt.xlim([0, 256])

plt.show()

fig = plt.figure()

# Create subplot
ax = fig.add_subplot(131)
# index 1 is G, index 0 is B
# We want two channels so [0, 1] instead of [0]
# 32 bins instead of 256 * 256
# Range is [0, 256, 0, 256]
hist = cv2.calcHist([channels[1], channels[0]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

# Show the size and get the number of values (width * height)
print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

plt.show()

# 3-D Histogram
## Basically get all three channels, 8 bins each, 256 range
hist = cv2.calcHist([image], [0, 1, 2],
                    None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

cv2.waitKey(0)