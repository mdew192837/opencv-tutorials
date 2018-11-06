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
# cv2.imshow("Original", image)

# Get the RGB values
# Remember in OpenCV it's backwards (B, G, R)
(B, G, R) = cv2.split(resized_image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

# Showing the color in the channels
zeros = np.zeros(resized_image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()