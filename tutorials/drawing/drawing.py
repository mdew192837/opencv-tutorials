import numpy as np
import cv2

# 300 height * 300 width * 3 channels (BGR)
# Unsigned int so we can go from 0 to 255
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Drawing time!
green = (0, 255, 0)

# Green line from top left to bottom right corner
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
# Red line from bottom left to top right
# Make the red line thicker
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# This also has a delay that you can use
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
# To get a filled in rectangle, just pass in a negative value
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Re-initialize canvas to be blank after!
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)