import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 

def movetofarmer():
        
    aut.moveTo(651, 82)
    aut.click()
    time.sleep(20)

def buy_pots():
    aut.moveTo(425, 115)
    aut.click()
    aut.press("esc")

def hop_world():
    # Define a static variable to keep track of the counter
    if not hasattr(hop_world, 'counter'):
        hop_world.counter = 531

    # Move to the target location
    aut.moveTo(430, 440)
    aut.click()

    # Write the current hop number
    aut.write("::hop {}".format(hop_world.counter))
    aut.press("enter")
    time.sleep(12)
    aut.moveTo(647, 213)
    aut.click()

    # Increment the counter
    hop_world.counter += 1

    # Reset the counter to 531 if it exceeds 535
    if hop_world.counter > 535:
        hop_world.counter = 531

def detect_farmer():
    print("detecting farmer..")
# Define the region of interest (ROI) coordinates
    roi_top_left = (7, 31)
    roi_bottom_right = (519, 364)
    screen_width, screen_height = aut.size()

    # Scale the ROI coordinates to screen resolution
    roi_top_left_scaled = (int(roi_top_left[0] * screen_width / 1920), int(roi_top_left[1] * screen_height / 1080))
    roi_bottom_right_scaled = (int(roi_bottom_right[0] * screen_width / 1920), int(roi_bottom_right[1] * screen_height / 1080))

    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                        roi_bottom_right[0] - roi_top_left[0], 
                                        roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


    # Convert the filtered image to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template1 = cv.imread('farmer.png', cv.IMREAD_GRAYSCALE)
    template2 = cv.imread('farmer2.png', cv.IMREAD_GRAYSCALE)
    template3 = cv.imread('farmer3.png', cv.IMREAD_GRAYSCALE)
    template4 = cv.imread('farmer4.png', cv.IMREAD_GRAYSCALE)

    templates = [template1, template2, template3, template4]

    # Blur both the grayscale image and the template
    blur = cv.blur(grayscale_img, (3,3))
    blur1 = cv.blur(template1, (3,3))

    # Apply Canny edge detection to both images
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)
    # cv.imshow("1", canny)
    # cv.imshow("2", canny1)
    # cv.waitKey(0)
    # cv.destroyAllWindows
    for idx, template in enumerate(templates):
        # Apply template matching
        result = cv.matchTemplate(grayscale_img, template, cv.TM_CCOEFF_NORMED)

        # Define a threshold for the match
        threshold = 0.7

        # Get the location of the best match
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # Check if the maximum match value is above the threshold
        if max_val >= threshold:
            print("Match found! not going to eat")
            # Convert the coordinates to real screen coordinates
            max_x = max_loc[0] * (roi_bottom_right[0] - roi_top_left[0]) / grayscale_img.shape[1] + roi_top_left[0]
            max_y = max_loc[1] * (roi_bottom_right[1] - roi_top_left[1]) / grayscale_img.shape[0] + roi_top_left[1]
            template_width = template.shape[1]
            template_height = template.shape[0]
            # Convert the matched location to global screen coordinates
            global_max_x = max_x + roi_top_left_scaled[0]
            global_max_y = max_y + roi_top_left_scaled[1]
            print("Template {} matched. Max value: {}, Global location: x={}, y={}, width={}, height={}".format(idx+1, max_val, global_max_x, global_max_y, template_width, template_height))

            aut.click(global_max_x - 4, global_max_y - 20)
            time.sleep(0.1)
            aut.click(global_max_x - 4, global_max_y - 20)
            time.sleep(3)
            buy_pots()
        else:
            print("Template {} not found in the screenshot".format(idx+1))

def detect_bank():
    print("detecting farmer..")
# Define the region of interest (ROI) coordinates
    roi_top_left = (620, 130)
    roi_bottom_right = (682, 158)
    screen_width, screen_height = aut.size()

    # Scale the ROI coordinates to screen resolution
    roi_top_left_scaled = (int(roi_top_left[0] * screen_width / 1920), int(roi_top_left[1] * screen_height / 1080))
    roi_bottom_right_scaled = (int(roi_bottom_right[0] * screen_width / 1920), int(roi_bottom_right[1] * screen_height / 1080))

    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                        roi_bottom_right[0] - roi_top_left[0], 
                                        roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


    # Convert the filtered image to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template1 = cv.imread('bankikon.png', cv.IMREAD_GRAYSCALE)

    # Blur both the grayscale image and the template
    blur = cv.blur(grayscale_img, (3,3))
    blur1 = cv.blur(template1, (3,3))

    # Apply Canny edge detection to both images
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)
    # cv.imshow("1", canny)
    # cv.imshow("2", canny1)
    # cv.waitKey(0)
    # cv.destroyAllWindows
        # Apply template matching
    result = cv.matchTemplate(grayscale_img, template1, cv.TM_CCOEFF_NORMED)

        # Define a threshold for the match
    threshold = 0.1

        # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # Check if the maximum match value is above the threshold
    if max_val >= threshold:
            
            # Convert the coordinates to real screen coordinates
            # max_x = max_loc[0] * (roi_bottom_right[0] - roi_top_left[0]) / grayscale_img.shape[1] + roi_top_left[0]
            # max_y = max_loc[1] * (roi_bottom_right[1] - roi_top_left[1]) / grayscale_img.shape[0] + roi_top_left[1]
            # Convert the matched location to global screen coordinates
            global_max_x = max_loc[0] + roi_top_left_scaled[0]
            global_max_y = max_loc[1] + roi_top_left_scaled[1]

            aut.click(global_max_x - 4, global_max_y - 20)
            time.sleep(0.1)
            aut.click(global_max_x - 4, global_max_y - 20)
            time.sleep(3)
            
    else:
            print("Template not found")

# Call the function
detect_bank()