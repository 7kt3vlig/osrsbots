import pyautogui as aut
import numpy as np
import cv2 as cv
from pynput.keyboard import Key, Listener
import math
import time 
#kamera 616 


def hittarosa():

    region = (8, 31, 520, 365)  # Define your capture region here

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
    
    if len(contours) == 0:
        print("No cyan shapes detected in the mask.")
        return

    closest_distance = float('inf')  # Initialize a variable to track the shortest distance
    closest_center = None  # Track the closest center coordinates

    # Loop through the contours and detect cyan shapes
    for i, contour in enumerate(contours):
        # Get the bounding box coordinates for the contour
        x, y, w, h = cv.boundingRect(contour)
        print(f"Contour {i}: Position (x={x}, y={y}), Dimensions (w={w}, h={h})")

        # Skip small shapes
        if w < 3 or h < 3:
            print(f"Contour {i} skipped: too small (less than 13x13 pixels).")
            continue

        # Check for regular cyan shapes (larger than 13x13)
        center_x = x + w // 2
        center_y = y + h // 2

        # Adjust for the region offset to get absolute screen coordinates
        absolute_center_x = center_x + region[0]
        absolute_center_y = center_y + region[1]

        # Calculate the Euclidean distance from the target point (x636, y349)
        distance = np.sqrt((absolute_center_x - target_x) ** 2 + (absolute_center_y - target_y) ** 2)

        print(f"Contour {i}: Center at ({absolute_center_x}, {absolute_center_y}), Distance from target: {distance:.2f}")

        # Update the closest shape if this one is closer
        if distance < closest_distance:
            closest_distance = distance
            closest_center = (absolute_center_x, absolute_center_y)
            print(f"Contour {i} is now the closest shape.")

        # Detect potential lines (width or height greater than 20 pixels)
        if w > 20 or h > 20:
            aspect_ratio = max(w, h) / min(w, h) if min(w, h) > 0 else float('inf')
            if aspect_ratio > 4:  # Aspect ratio check to confirm it's line-like
                print(f"Contour {i}: Detected a line at (x={x}, y={y}) with dimensions (w={w}, h={h}), Aspect Ratio: {aspect_ratio:.2f}")
            else:
                print(f"Contour {i}: Large shape detected but not2 line (aspect ratio {aspect_ratio:.2f}).")

    # If a closest center was found, click on it
    if closest_center is not None:
        aut.moveTo(closest_center[0], closest_center[1])
        aut.click(button="right")
        aut.moveTo(closest_center[0], closest_center[1] + 40)
        aut.click()
        print(f"Clicked on the closest cyan shape at {closest_center} with a distance of {closest_distance:.2f}")
    else:
        print("No valid cyan shapes were found to click on.")

def hittarosa2():

    region = (8, 31, 520, 365)  # Define your capture region here

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
    
    if len(contours) == 0:
        print("No cyan shapes detected in the mask.")
        return

    closest_distance = float('inf')  # Initialize a variable to track the shortest distance
    closest_center = None  # Track the closest center coordinates

    # Loop through the contours and detect cyan shapes
    for i, contour in enumerate(contours):
        # Get the bounding box coordinates for the contour
        x, y, w, h = cv.boundingRect(contour)
        print(f"Contour {i}: Position (x={x}, y={y}), Dimensions (w={w}, h={h})")

        # Skip small shapes
        if w < 3 or h < 3:
            print(f"Contour {i} skipped: too small (less than 13x13 pixels).")
            continue

        # Check for regular cyan shapes (larger than 13x13)
        center_x = x + w // 2
        center_y = y + h // 2

        # Adjust for the region offset to get absolute screen coordinates
        absolute_center_x = center_x + region[0]
        absolute_center_y = center_y + region[1]

        # Calculate the Euclidean distance from the target point (x636, y349)
        distance = np.sqrt((absolute_center_x - target_x) ** 2 + (absolute_center_y - target_y) ** 2)

        print(f"Contour {i}: Center at ({absolute_center_x}, {absolute_center_y}), Distance from target: {distance:.2f}")

        # Update the closest shape if this one is closer
        if distance < closest_distance:
            closest_distance = distance
            closest_center = (absolute_center_x, absolute_center_y)
            print(f"Contour {i} is now the closest shape.")

        # Detect potential lines (width or height greater than 20 pixels)
        if w > 20 or h > 20:
            aspect_ratio = max(w, h) / min(w, h) if min(w, h) > 0 else float('inf')
            if aspect_ratio > 4:  # Aspect ratio check to confirm it's line-like
                print(f"Contour {i}: Detected a line at (x={x}, y={y}) with dimensions (w={w}, h={h}), Aspect Ratio: {aspect_ratio:.2f}")
            else:
                print(f"Contour {i}: Large shape detected but not2 line (aspect ratio {aspect_ratio:.2f}).")

    # If a closest center was found, click on it
    if closest_center is not None:
        aut.moveTo(closest_center[0], closest_center[1])
        aut.click()
        print(f"Clicked on the closest cyan shape at {closest_center} with a distance of {closest_distance:.2f}")
    else:
        print("No valid cyan shapes were found to click on.")


def betty():
 
    for i in range (1):
        hittarosa()
        time.sleep(3)
        aut.press("space")
        time.sleep(1) 
        aut.press("2")
        time.sleep(1)
        aut.press("space")
        time.sleep(1)
        aut.press("space")
        time.sleep(1) 
        aut.press("1")
        time.sleep(1)
        aut.press("space")
        time.sleep(1)
        
        for i in range (26):
            hittarosa()
            time.sleep(1)
            aut.press("space")
            time.sleep(1) 
            aut.press("2")
            time.sleep(1)
            aut.press("space")
            time.sleep(1)
            aut.press("space")
            time.sleep(1) 
            aut.press("1")
            time.sleep(1)
            aut.press("space")
            time.sleep(1)

    aut.moveTo(676, 162)  
    aut.click()
    time.sleep(12)
    hittarosa2()
    time.sleep(10)
    aut.moveTo(148, 124)  
    aut.click()
    time.sleep(2)
    aut.moveTo(596, 67)  
    aut.click()
    time.sleep(13)
    


def fillcans():

    aut.moveTo(2453, 458)  
    time.sleep(1)
    aut.press("space")
    time.sleep(0.7)


#kamera -159 
def zentrees():

    hittarosa2()
    time.sleep(4)



    # aut.moveTo(2589, 364)  #trapporna
    # time.sleep(1)
    # aut.click()
    # time.sleep(2)


    # aut.moveTo(2168, 651)  #banken
    # time.sleep(1)
    # aut.click()
    # time.sleep(11)

    aut.moveTo(325, 92)  #tabben 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(670, 260)  #deposit kanna 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(384, 165)  #ta kanna 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(238, 167)  #ta dye
    aut.click()
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(284, 168)  #ta plants
    aut.click()
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(333, 166)  #ta sand 
    aut.click()
    time.sleep(0.6)

    aut.press("esc")
    time.sleep(0.2)

    aut.moveTo(585, 255)  #tp house
    aut.click()
    time.sleep(5)

    aut.moveTo(335, 159)  #gå till trädet
    aut.click()
    time.sleep(2.5)

    for i in range (3):
        aut.moveTo(277, 171)  #build
        aut.click()
        time.sleep(1)
        aut.press("1")
        time.sleep(1.4)


        aut.moveTo(277, 171)  #remove
        aut.click()    
        time.sleep(1)
        aut.press("1")
        time.sleep(1.4)

    
    aut.moveTo(625, 259)  #craftingcape
    aut.click()
    time.sleep(3)

 
# -159 seedpod , 330 ny crafting guild 
while True:
        
    zentrees()

#  for i in range (27):
    
#      betty()
     

 