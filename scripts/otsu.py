import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

# Read image
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)

# Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply the Otsu binarization
# Get the retvalue and the threshold
# 0 for threshold, let OTSU do it
# Returns the retvalue and the thresholded image
ret, thresh = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Plot the code
## https://www.kaggle.com/javidimail/nuclei-detection-with-opencv
plt.figure(figsize=(15,5))
images = [blurred_image, 0, thresh]
titles = ['Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
plt.subplot(1,3,1),plt.imshow(images[0],'gray')
plt.title(titles[0]), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.hist(images[0].ravel(),256)
plt.title(titles[1]), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(images[2],'gray')
plt.title(titles[2]), plt.xticks([]), plt.yticks([])

plt.show()

# Old code for showing images
## cv2.imshow("Original", image)
## cv2.imshow("Thresholded", thresh)
processed_image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
processed_image = cv2.drawContours(processed_image, contours, -1, (255,255,255), 3)
plt.figure(figsize=(10,10))
plt.subplot(1,2,1),plt.title('Original Image'),plt.imshow(image)#,'red')
plt.subplot(1,2,2),plt.title('OpenCV.findContours'),plt.imshow(processed_image,'gray')#,'red')

plt.show()

print('number of detected contours: ',len(contours))

cv2.waitKey(0)