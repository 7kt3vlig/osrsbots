import random
from PIL import Image, ImageGrab
import numpy as np 
import cv2 as cv
import pyautogui
import time 

for i in range(20):
    # Capture the screenshot
    foto = ImageGrab.grab(bbox=(304, 28, 815, 361))
    foto.save("test.png")
    # Read the image
    img = cv.imread("test.png")
    if img is None:
        print("Error: Unable to read the image.")
        continue
    # Convert the image to HSV color space
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # Define the lower and upper bounds for the light cyan color in HSV format
    lower_bound = np.array([90, 100, 150])
    upper_bound = np.array([110, 255, 255])
    # Threshold the image to create a binary mask highlighting regions with the specified color
    mask = cv.inRange(hsv, lower_bound, upper_bound)
    # Find contours in the binary mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if not contours:  # Check if no contours are found
        print("No contours found.")
        continue
    # Draw contours on a blank image
    contour_img = np.zeros_like(img)
    cv.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    # Select one contour randomly
    selected_contour = random.choice(contours)
    # Calculate the centroid (center of mass) of the selected contour
    M = cv.moments(selected_contour)
    if M["m00"] != 0:  # Check if the contour area is non-zero
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        # Move the mouse cursor to the centroid
        pyautogui.moveTo(cx + 302, cy + 28)
        pyautogui.click()
        pyautogui.moveTo(836, 257)
        time.sleep(8)