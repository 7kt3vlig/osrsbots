import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os



aut.moveTo(1265, 470)
aut.click()
time.sleep(30)

aut.moveTo(790, 192)
aut.click()

def gronring():
    top_left = (324, 282)
    bottom_right = (388, 342)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("gamefinished.png")
    
    if template is None:
        print("Template image gronring.png not found or unable to load.")
        return False

    # Define the threshold for a match
    threshold = 0.7

    # Capture the screenshot of the specified region using pyautogui
    try:
        screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                            bottom_right[0] - top_left[0],
                                            bottom_right[1] - top_left[1]))
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Perform template matching using the color image
    result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
    
    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("Printing matching values for gronring:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        
        time.sleep(3)
        aut.moveTo(1245, 495)
        aut.click()
        return True
    else:
        print("No match found above the threshold for gronring.")
        return False