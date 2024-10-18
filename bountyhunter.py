import pyautogui as aut
import numpy as np
import cv2 as cv
from pynput.keyboard import Key, Listener
import math
import time 


#melee

gmaul_template = cv.imread("gmaul.png")

#extras 

halfhpbar_template = cv.imread("halfhptemplate.png")

aut.PAUSE = 0.04 # Remove any pauses between actions



def halfhpbar():
    top_left = (644, 658)
    bottom_right = (803, 680)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("halfhpbar.png")
    
    if template is None:
        print("Template image halfhpbar.png not found or unable to load.")
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
    print("Printing matching values for halfhpbar:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for halfhpbar.")
       
        return True
    else:
        print("No match found above the threshold for halfhpbar.")
        return False






















def find_and_click_opponent():
   # Define the region to capture (x1, y1, width, height)
    region = (313, 135, 645, 429)  # Define your capture region here

    # Target coordinates (to find the closest shape to these)
    target_x = 636
    target_y = 349

    # Capture the screen in the defined region
    print(f"Capturing region: {region}")
    screenshot = aut.screenshot(region=region)
    screenshot_np = np.array(screenshot)

    # Convert the image from RGB to BGR format (OpenCV uses BGR)
    screenshot_bgr = cv.cvtColor(screenshot_np, cv.COLOR_RGB2BGR)

    # Convert BGR to HSV color space
    hsv_image = cv.cvtColor(screenshot_bgr, cv.COLOR_BGR2HSV)

    # Define the lower and upper bounds for cyan in HSV
    lower_cyan = np.array([145, 100, 100])  # Adjust saturation and value as needed
    upper_cyan = np.array([155, 255, 255])

    # Create a mask for the cyan color
    print("Creating mask for cyan color detection...")
    mask = cv.inRange(hsv_image, lower_cyan, upper_cyan)

    # Find contours in the masked image
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    print(f"Number of contours found: {len(contours)}")
    
    if len(contours) == 1:
        print("No cyan shapes detected in the mask.")
        return



def find_matches(templates, coordinates):
    # Initialize a list to store the coordinates of detected items
    matches = []

    # Define the threshold for a match
    threshold = 0.7

    # Capture the screenshot of the specified region using pyautogui
    try:
        screenshot = aut.screenshot(region=coordinates)
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return matches

    # Check each template for matches
    for template_name, template in templates:
        result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        print(f"Checking {template_name}: Min value: {min_val}, Max value: {max_val}, Max location: {max_loc}")

        # If the match is above the threshold, store the center coordinates
        if max_val >= threshold:
            center_x = max_loc[0] + (template.shape[1] // 2)  # center x
            center_y = max_loc[1] + (template.shape[0] // 2)  # center y
            matches.append((center_x + coordinates[0], center_y + coordinates[1]))  # Adjust for region offset
            print(f"Match found for {template_name} at ({center_x + coordinates[0]}, {center_y + coordinates[1]})")

    return matches

def click_matches(matches):
    for x, y in matches:
        aut.moveTo(x, y)  # Move to each match
        aut.click()       # Click on it
        print(f"Clicked on item at ({x}, {y})")
        
def checkmeleeitems():

    area_to_check = (999, 412, 238, 358)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [("gmaul", gmaul_template)
                          
        
    ]

    # Find matches in the specified area
    matches = find_matches(templates_to_check, area_to_check)
    
    if matches:
        click_matches(matches)  # Click all found items
    else:
        print("No items matched in the specified area.")


def function_t():
    find_and_click_opponent()
    time.sleep(2)
    aut.press("2")
    checkmeleeitems()
    aut.press("1") #spec
    aut.moveTo(1100, 665)#
    aut.click()
    aut.click()
    aut.press("2") #inv 
    find_and_click_opponent()
    aut.click()






# Listener functions
def on_press(key):
    try:
        # Check if specific keys are pressed and execute respective functions
        if key.char == 't':
            function_t()
        
    except AttributeError:
        # Ignore special keys that do not have a 'char' attribute
        pass

def on_release(key):
    if key == Key.f12:
        # Stop listener if Escape key is pressed
        return False

# Start listening
print("Program is running. Press 'e' to check for items.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()












#644, 658 
#803 680


