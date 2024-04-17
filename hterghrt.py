import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 


def refilldodgyneck():
    print("checking dodgyneck..")

    aut.moveTo(582, 260)#töm pouches 
    time.sleep(0.2)
    aut.click()
    aut.moveTo(680, 215)#gear tab
    time.sleep(0.2)
    aut.click()

# Define the region of interest (ROI) coordinates
    roi_top_left = (627, 275)
    roi_bottom_right = (664, 310)

    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                        roi_bottom_right[0] - roi_top_left[0], 
                                        roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


    # Convert the filtered image to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('dodgyneck.png', cv.IMREAD_GRAYSCALE)

    # Blur both the grayscale image and the template
    blur = cv.blur(grayscale_img, (3,3))
    blur1 = cv.blur(template, (3,3))

    # Apply Canny edge detection to both images
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)

    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

        # Define a threshold for the match
    threshold = 0.53

    # Get the location of the best match
    _, max_val, _, _ = cv.minMaxLoc(result)

    # Check if the maximum match value is above the threshold
    if max_val >= threshold:
        print("Match found! not going to get necklace")
        print("Max value:", max_val)
        aut.moveTo(650,215)#tillbaka till inventory tabben
        time.sleep(0.2)
        aut.click()
    else:
        print("No match found, going to get a new necklace..")
        print("Max value:", max_val)
        aut.moveTo(650,215)#tillbaka till inventory tabben
        time.sleep(0.2)
        aut.click()
        aut.moveTo(429, 186)#bank
        aut.click()
        time.sleep(3)
        aut.moveTo(239, 126)#neck
        aut.click()
        time.sleep(0.6)
        aut.press("esc")

        aut.moveTo(582, 260)#wear necklace 
        time.sleep(0.2)
        aut.click()
        time.sleep(0.6)

        aut.moveTo(73, 177)#tillbaka / ardy knight i banken
        aut.click()
        time.sleep(2)

refilldodgyneck()