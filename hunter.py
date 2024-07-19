import pyautogui 
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os

def autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            pyautogui.keyDown("shift")
            pyautogui.moveTo(x, y)
            pyautogui.click()
            pyautogui.keyUp("shift")

# Define the starting point and offsets
start_x = 3160
start_y = 490
x_offset = 88
y_offset = 73
num_rows = 7
num_cols = 4

        
autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset)


def hittakebbit():
    top_left = (80, 100)
    bottom_right = (975, 615)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template images in BGR color
    templates = [
        cv.imread("kebbit.png"),
        cv.imread("kebbit2.png"),
        cv.imread("kebbit3.png")
    ]
    
    # Check if all templates are loaded correctly
    for i, template in enumerate(templates):
        if template is None:
            print(f"Template image kebbit{i+1}.png not found or unable to load.")
            return

    # Define the threshold for a match
    threshold = 0.75

    condition_met = False
    while not condition_met:
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
                pyautogui.click(click_x, click_y)
                condition_met = True
                break

        if not condition_met:
            print("No match found above the threshold. Retrying...")
            time.sleep(1)  # Add a delay to avoid overloading the CPU with continuous screenshots

    print("Match found and clicked.")

def takebbit():
    top_left = (80, 100)
    bottom_right = (975, 615)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template images in BGR color
    templates = [
        cv.imread("pil.png"),
        cv.imread("pil2.png"),
        cv.imread("pil3.png")
    ]
    
    # Check if all templates are loaded correctly
    for i, template in enumerate(templates):
        if template is None:
            print(f"Template image kebbit{i+1}.png not found or unable to load.")
            return

    # Define the threshold for a match
    threshold = 0.75

    condition_met = False
    while not condition_met:
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
                click_y = center_y + top_left[1] + 40
                pyautogui.click(click_x, click_y)
                condition_met = True
                break

        if not condition_met:
            print("No match found above the threshold. Retrying...")
            time.sleep(1)  # Add a delay to avoid overloading the CPU with continuous screenshots

    print("Match found and clicked.")


# while True:
        
#     hittakebbit()
#     time.sleep(5)
#     takebbit()

