from PIL import Image, ImageGrab
import numpy as np 
import cv2 as cv
import pyautogui
import random 

# Capture the screenshot
foto = ImageGrab.grab(bbox=(302, 28, 816, 361))
foto.save("test.png")
# Read the image
img = cv.imread("test.png")
# Convert the image to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# Define the lower and upper bounds for the light cyan color in HSV format
lower_bound = np.array([85, 100, 100])
upper_bound = np.array([100, 255, 255])
# Threshold the image to create a binary mask highlighting regions with the specified color
mask = cv.inRange(hsv, lower_bound, upper_bound)
# Find contours in the binary mask
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank image
contour_img = np.zeros_like(img)
cv.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

# Calculate and move mouse to the centroid of each contour
for contour in contours:
    # Calculate the centroid (center of mass) of the contour
    M = cv.moments(contour)
    if M["m00"] != 0:  # Check if the contour area is non-zero
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        
        # Move the mouse cursor to the centroid
        pyautogui.moveTo(cx + 302, cy + 28)
        pyautogui.click()

# Display the image with contours
cv.imshow("Contours", contour_img)
cv.waitKey(0)