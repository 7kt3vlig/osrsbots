import pyautogui as aut
import numpy
import cv2 as cv
import time 
import numpy as np

aut.PAUSE = 0

event_template = cv.imread("lapp.png")
event_template2 = cv.imread("lapp2.png")


def restart():
    aut.moveTo(1625, 715) # 
    time.sleep(0.2)
    aut.click()
    time.sleep(1)


def klicka():
    

    # aut.moveTo(1625, 715) # 
    # time.sleep(0.2)
    # aut.mouseDown(button="left")
    # aut.mouseUp(button="left")

   # Coordinates for the region to capture
    top_left = (818, 319)
    bottom_right = (1259, 993)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("lapp.png", cv.IMREAD_COLOR)
    
    
    # Check if template image is successfully loaded
    if template is None:
        print("Template image EVENT.png not found or unable to load.")
        return False

    # Define the threshold for a match
    threshold = 0.995

    # Capture the screenshot of the specified region using pyautogui
    try:
        screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                           bottom_right[0] - top_left[0],
                                           bottom_right[1] - top_left[1]))
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Perform template matching
    result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
    
    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(f"Matching values:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold
    if max_val >= threshold:
        print(f"Match found with confidence {max_val}.")
        
        # Calculate the center of the match
        match_center = (max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2)
        print(f"Clicking at the center of the match: {match_center}")
        
        # Adjust the coordinates by adding the top_left offset (to make them relative to the whole screen)
        screen_x = top_left[0] + match_center[0]
        screen_y = top_left[1] + match_center[1]

        print(f"Adjusted click position: ({screen_x}, {screen_y})")
        
        # Move the mouse to the center of the match in the screenshot region
        aut.moveTo(screen_x, screen_y)
        
        # Click and hold
        aut.click()
        aut.click()
        
        return True

    # If no match is found above the threshold, return False
    print("No match found above the threshold.")
    return False


def klickainte():

    # aut.moveTo(1625, 715) # 
    # time.sleep(0.2)
    # aut.mouseDown(button="left")
    # aut.mouseUp(button="left")

   # Coordinates for the region to capture
    top_left = (818, 319)
    bottom_right = (1259, 993)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("lapp2.png")
    
    
    # Check if template image is successfully loaded
    if template is None:
        print("Template image EVENT.png not found or unable to load.")
        return False

    # Define the threshold for a match
    threshold = 0.995

    # Capture the screenshot of the specified region using pyautogui
    try:
        screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                           bottom_right[0] - top_left[0],
                                           bottom_right[1] - top_left[1]))
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Perform template matching
    result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
    
    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(f"Matching values:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold
    if max_val >= threshold:
        print(f"Match found with confidence {max_val}.")
        
        # Calculate the center of the match
        match_center = (max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2)
        print(f"Clicking at the center of the match: {match_center}")
        
        # Adjust the coordinates by adding the top_left offset (to make them relative to the whole screen)
        screen_x = top_left[0] + match_center[0]
        screen_y = top_left[1] + match_center[1]

        print(f"Adjusted click position: ({screen_x}, {screen_y})")
        
        # Move the mouse to the center of the match in the screenshot region
       
        
        # Click and hold
        # aut.click()
        
        return True
    else:
        return False

while True:
    # klicka()
    aut.moveTo(1405, 635)
    aut.click()
    time.sleep(2)
    aut.moveTo(1405, 920)
    aut.click()
    time.sleep(2)

    # aut.moveTo(1575, 835)
    # aut.click()
    # time.sleep(0.5)
    # aut.click()
    # time.sleep(0.5)

    # aut.moveTo(1625, 800)
    # aut.click()
    # time.sleep(0.5)
    
    
    
