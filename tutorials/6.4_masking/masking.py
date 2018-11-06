import argparse
import cv2

# Create the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

# Read in the image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Create the black mask canvas with a numpy zeros array
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
# Create the rectangle that is white at the center of the image
# Width 150, height 150
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)
cv2.imshow("Mask", mask)

# Apply Bitwise And
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)