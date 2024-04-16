import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os
import pytesseract
from PIL import Image


def ardyknight():
    print("Stealing..")
    aut.moveTo(63, 217)
    aut.click()
    time.sleep(0.6)


def detect_coin_pouches():

    print("checking pouches..")
    # Define the region of interest (ROI) coordinates
    roi_top_left = (560, 235)
    roi_bottom_right = (597, 272)

    # Take a screenshot of the specified region
    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                         roi_bottom_right[0] - roi_top_left[0], 
                                         roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('coinpouches.png', cv.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv.matchTemplate(grayscale_img, template, cv.TM_CCOEFF_NORMED)

    # Define a threshold for the match
    threshold = 0.9

    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Check if the maximum match value is above the threshold
    if max_val >= threshold:
        print("detected pouches, clicking them")
        aut.moveTo(582, 260)
        time.sleep(0.2)
        aut.click()
    else:
        print("No match found, continuing with the script ")



def detect_hp():
    print("checking hp..")
    # Define the region of interest (ROI) coordinates
    roi_top_left = (525, 83)
    roi_bottom_right = (543, 95)

    # Take a screenshot of the specified region
    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                         roi_bottom_right[0] - roi_top_left[0], 
                                         roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('hp.png', cv.IMREAD_GRAYSCALE)

    # Threshold the template image to create a mask
    _, mask = cv.threshold(template, 220, 255, cv.THRESH_BINARY)

    # Find contours in the mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw contours on the template image (for visualization)
    template_with_contours = cv.drawContours(cv.cvtColor(template, cv.COLOR_GRAY2BGR), contours, -1, (0, 255, 0), 2)

    # Perform template matching
    result = cv.matchTemplate(grayscale_img, template, cv.TM_CCOEFF_NORMED)

    # Define a threshold for the match
    threshold = 0.8

    # Get the location of the best match
    _, max_val, _, _ = cv.minMaxLoc(result)

    # Check if the maximum match value is above the threshold
    if max_val >= threshold:
        print("Match found! not going to eat")
        print("Max value:", max_val)
        
    else:
        print("No match found, going to eat..")
        print("Max value:", max_val)
        aut.moveTo(582, 333)  
        time.sleep(0.2)
        aut.click()
        


def kollahp():
    # Load the image containing the number "73"
    image = Image.open('hp.png')

    # Perform OCR using pytesseract
    ocr_result = pytesseract.image_to_string(image, config='--psm 6')

    # Check if "73" is found in the OCR result
    if '73' in ocr_result:
        print("Number 73 found:", ocr_result)
    else:
        print("Number 73 not found in the image.")

kollahp()





