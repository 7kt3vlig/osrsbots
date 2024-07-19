import pyautogui as aut
import cv2 as cv
import numpy as np
import time
import threading 


def grontrap():
    top_left = (299, 264)
    bottom_right = (430, 395)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template images in BGR color
    
    template = cv.imread("gronring.png")

    # Define the threshold for a match
    threshold = 0.7

    condition_met = False
    while not condition_met:
        # Capture the screenshot of the specified region using pyautogui
        try:
            screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                                    bottom_right[0] - top_left[0],
                                                    bottom_right[1] - top_left[1]))
            screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
        except Exception as e:
            print(f"Error capturing screenshot with pyautogui: {e}")
            return
        
        
        result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
        
        # Get the best match position
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print("Printing matching values:")
        print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
        
        # If the match is above the threshold, click on the position
        if max_val >= threshold:
            time.sleep(1)
            template_height, template_width = template.shape[:2]
            center_x = max_loc[0] + template_width // 2
            center_y = max_loc[1] + template_height // 2
            click_x = center_x + top_left[0]
            click_y = center_y + top_left[1]
            aut.click(click_x + 100, click_y + 20)
            condition_met = True
            break

        if not condition_met:
            print("No match found above the threshold. Retrying...")
            time.sleep(1)  # Add a delay to avoid overloading the CPU with continuous screenshots

    print("Match found and clicked.")



def placebanana():

    aut.moveTo(3257, 487)
    aut.click(button="right")
    aut.moveTo(3257, 487)
    aut.click()


def drop():
    aut.moveTo(3160, 490)
    aut.click()



def click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            aut.moveTo(x, y)
            aut.click(button="right")
            aut.moveTo(x, y + 86)
            aut.click()
            time.sleep(1)
            aut.moveTo(2373, 377)
            aut.click()
            time.sleep(65)
            aut.moveTo(3160, 490)
            aut.click()



# Define the starting point and offsets
start_x = 3255
start_y = 490
x_offset = 88
y_offset = 73
num_rows = 7
num_cols = 4


# click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
            

grontrap()