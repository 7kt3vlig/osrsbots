import cv2 as cv
import pyautogui as aut
import numpy as np
import time

def ingenring():
    top_left = (324, 282)
    bottom_right = (388, 342)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("ingenring.png")
    
    if template is None:
        print("Template image ingenring.png not found or unable to load.")
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
    print("Printing matching values for ingenring:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for ingenring. Clicking on the position.")
       
        return True
    else:
        print("No match found above the threshold for ingenring.")
        return False

def gronring():
    top_left = (324, 282)
    bottom_right = (388, 342)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("gronring.png")
    
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
        print("Match found for gronring. Clicking on the position.")
        template_height, template_width = template.shape[:2]
        center_x = max_loc[0] + template_width // 2
        center_y = max_loc[1] + template_height // 2
        click_x = center_x + top_left[0]
        click_y = center_y + top_left[1]
        aut.moveTo(click_x + 100, click_y + 40)
        aut.click(click_x + 100, click_y + 40)
        time.sleep(3)
        aut.moveTo(1245, 495)
        aut.click()
        return True
    else:
        print("No match found above the threshold for gronring.")
        return False

def click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            for _ in range(5):
                aut.moveTo(x, y)
                aut.click(button="right")
                aut.moveTo(x, y + 86)
                aut.click()
                time.sleep(1)
                aut.moveTo(443, 371)
                aut.click()
                time.sleep(5)
                
                while True:
                    if ingenring():
                        break
                    if gronring():
                        break
                    time.sleep(1)  # Add a delay to avoid overloading the CPU

# Define the starting point and offsets
start_x = 1245
start_y = 565
x_offset = 88
y_offset = 73
num_rows = 4
num_cols = 4

click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset)