from __future__ import print_function
import argparse
import cv2

# Require image as an argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

# Read the image
image = cv2.imread(args["image"])

# Refer to the Jupyter Notebook to learn how to get and set individual pixels
# Note that values are stored as BGR instead of RGB

# Grab the top left 100 by 100 pixel block of pixels
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# Now let's make that green!
image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)