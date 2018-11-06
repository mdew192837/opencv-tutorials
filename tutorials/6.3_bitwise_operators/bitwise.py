import numpy as np
import cv2

# Create a 300 by 300 rectangle white canvas
rectangle = np.zeros((300, 300), dtype = "uint8")
# Create a rectangle from 25, 25 to 275, 275 that is black and is filled in
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# Create a new canvas
circle = np.zeros((300, 300), dtype = "uint8")
# Create a circle centered in the middle with radius 150 and filled in black
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)

cv2.waitKey(0)