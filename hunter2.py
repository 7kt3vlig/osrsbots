import pyautogui 
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os



def boxtrap():
    firstbox = (3165, 500) 
    secondbox = (3255, 500 )
    thirdbox = (3350, 500 )

    firstbox1 = (2719, 376) 
    secondbox1 = (2638, 379 )
    thirdbox1 = (2557, 378 )

    mittenavgubben = (565, 380)

    pyautogui.click(firstbox)
    time.sleep(5)
    pyautogui.click(secondbox)
    time.sleep(5)
    pyautogui.click(thirdbox)
    time.sleep(30)
    pyautogui.click(firstbox1)
    time.sleep(5)
    pyautogui.click(secondbox1)
    time.sleep(5)
    pyautogui.click(thirdbox1)
    time.sleep(30)

def checktrapcolor():
    
    top_left = (440, 350)
    bottom_right = (675, 420)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template images in BGR color
    templates = [
        cv.imread("redtrap.png"),
        cv.imread("greentrap.png"),
        cv.imread("fallentrap.png")
    ]
    
    # Check if all templates are loaded correctly
    for i, template in enumerate(templates):
        if template is None:
            print(f"Template image kebbit{i+1}.png not found or unable to load.")
            return

    # Define the threshold for a match
    threshold = 0.6

    while True:
        # Capture the screenshot of the specified region using pyautogui
        try:
            screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1],
                                                    bottom_right[0] - top_left[0],
                                                    bottom_right[1] - top_left[1]))
            screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
        except Exception as e:
            print(f"Error capturing screenshot with pyautogui: {e}")
            return
        
        # Perform template matching using color images for each template
        for template in templates:
            result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
            
            # Get the best match position
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("Printing matching values:")
            print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
            
            # If the match is above the threshold, click on the position
            if max_val >= threshold:
                template_height, template_width = template.shape[:2]
                center_x = max_loc[0] + template_width // 2
                center_y = max_loc[1] + template_height // 2
                click_x = center_x + top_left[0]
                click_y = center_y + top_left[1]
                time.sleep(1)
                pyautogui.click(click_x, click_y)
                pyautogui.click(click_x, click_y)
                pyautogui.moveTo(565, 380)
                time.sleep(5)
                break

        print("No match found above the threshold. Retrying...")
        time.sleep(1)  # Add a delay to avoid overloading the CPU with continuous screenshots



def checktrapcolor2():
    
    top_left = (520, 420)
    bottom_right = (595, 477)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template images in BGR color
    templates = [
        cv.imread("redtrap.png"),
        cv.imread("greentrap.png"),
        cv.imread("fallentrap.png")
    ]
    
    # Check if all templates are loaded correctly
    for i, template in enumerate(templates):
        if template is None:
            print(f"Template image kebbit{i+1}.png not found or unable to load.")
            return

    # Define the threshold for a match
    threshold = 0.6

    while True:
        # Capture the screenshot of the specified region using pyautogui
        try:
            screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1],
                                                    bottom_right[0] - top_left[0],
                                                    bottom_right[1] - top_left[1]))
            screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
        except Exception as e:
            print(f"Error capturing screenshot with pyautogui: {e}")
            return
        
        # Perform template matching using color images for each template
        for template in templates:
            result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
            
            # Get the best match position
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("Printing matching values:")
            print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
            
            # If the match is above the threshold, click on the position
            if max_val >= threshold:
                template_height, template_width = template.shape[:2]
                center_x = max_loc[0] + template_width // 2
                center_y = max_loc[1] + template_height // 2
                click_x = center_x + top_left[0]
                click_y = center_y + top_left[1]
                time.sleep(1)
                pyautogui.click(click_x, click_y)
                pyautogui.click(click_x, click_y)
                time.sleep(5)
                pyautogui.moveTo(633, 317)
                pyautogui.click()
                pyautogui.moveTo(565, 380)
                time.sleep(1)
                break

        print("No match found above the threshold. Retrying...")
        time.sleep(1)  # Add a delay to avoid overloading the CPU with continuous screenshots

while True:
        
    checktrapcolor()
    checktrapcolor2()