import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 
import numpy as np
import random


def hittarosa():

    region = (1154, 31, 1670, 365)  # Define your capture region here

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


def varrock():


    while True:

        aut.moveTo(138, 128) #hammer   
        aut.click()
        time.sleep(0.2)

        aut.moveTo(95, 126) #bar  
        time.sleep(0.2)
        aut.click()
        

        aut.press("esc")

        aut.moveTo(315, 361) #anvil 
        time.sleep(0.2)
        aut.click()
        time.sleep(5)


        aut.moveTo(366, 97) # chainbodys 
        time.sleep(0.2)
        aut.click()
        # time.sleep(81)

        for i in range (18):
            aut.moveTo(1320, 155) # runewild 
            time.sleep(0.2)
            aut.click()
            time.sleep(1)
            aut.moveTo(1670, 260) # runewild 
            time.sleep(0.2)
            aut.keyDown("shift")
            aut.click()
            aut.keyUp("shift")
            time.sleep(2.6)


        aut.moveTo(248, 107) # banken 
        time.sleep(0.2)
        aut.click()
        time.sleep(5)

        aut.moveTo(450, 340) # banka allt 
        time.sleep(0.2)
        aut.click()
        time.sleep(0.4)

#cam 400
def prif():

     while True:

        hittarosa()

        time.sleep(3.5)

        aut.moveTo(450, 340) # banka allt 
        time.sleep(0.2)
        aut.click()
        time.sleep(0.4)

        aut.moveTo(138, 128) #hammer   
        aut.click()
        time.sleep(0.2)

        aut.moveTo(95, 126) #bar  
        time.sleep(0.2)
        aut.click()
        

        aut.press("esc")

        aut.moveTo(20, 286) #anvil 
        time.sleep(0.2)
        aut.click()
        time.sleep(3.5)


        # aut.moveTo(365, 100) # darts
        # aut.moveTo(45, 265) # longsword
        # aut.moveTo(285, 205) # sq shield
        aut.moveTo(205, 265) # pl8
        time.sleep(0.2)
        aut.click()
        time.sleep(15) #40 LONG x2, 81 dart x1, 15 pl8 x5

def superheat():

    while True:
        aut.moveTo(367, 204)  #banker
        time.sleep(0.2)
        aut.click()
        time.sleep(0.5)

        aut.moveTo(625, 255)  #banka bars 
        time.sleep(0.2)
        aut.click()
        time.sleep(0.5)

        aut.moveTo(190, 165) #ta coal  
        aut.click()
        aut.click()
        aut.click()
        time.sleep(0.2)

        aut.moveTo(190, 200) #ta runite  
        aut.click()
        time.sleep(0.2)

        
        aut.press("esc")
        time.sleep(0.2)

        # aut.press("4")

        for i in range (3):
            aut.moveTo(650, 320) #superheat 
            aut.click()
            time.sleep(0.2)

            aut.moveTo(710, 475) #runite ore
            aut.click()
            time.sleep(1)  

# superheat()
# prif()

#kamera 188 prif 
# for i in range (100):
#     aut.moveTo(1251, 354) #runite ore
#     aut.click()
#     time.sleep(5)

#     aut.press("space")

#     time.sleep(10)

#     aut.moveTo(1533, 109) #bank
#     aut.click()
#     time.sleep(5)


#     aut.moveTo(1600, 340) #banka allt
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1240, 161) #ta ore
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1290, 128) #ta ore 
#     aut.click()
#     time.sleep(1)

#     aut.press("esc")
#     time.sleep(0.7)

#dart tips 190 cam
# for i in range (100):
#     aut.moveTo(1270, 282, duration=0.2) # anvil
#     aut.click()
#     time.sleep(5)

#     aut.moveTo(1500, 100, duration=0.2) # dart
#     aut.click()
#     time.sleep(5)

#     time.sleep(random.uniform(85, 115))

#     aut.moveTo(1524, 127, duration=0.2) # banker
#     aut.click()
#     time.sleep(5)


#     aut.moveTo(1775, 259, duration=0.2) # banka allt
#     aut.click()
#     time.sleep(1)


#     aut.moveTo(1339, 128, duration=0.2) #ta bars
#     aut.click()
#     time.sleep(1)

#     aut.press("esc")
#     time.sleep(0.7)

# kanonkulor incinidary eller w.e. de heter 


# for i in range (100):
#     aut.moveTo(1515, 225, duration=0.2) # anvil
#     aut.click()
#     time.sleep(1)
#     aut.press("space")
#     time.sleep(random.uniform(30, 70))


# while True:
        
#     aut.click()
#     time.sleep(20)

# #Melee crabs training 
# # #kamera 566 
# for i in range (100):
#     aut.moveTo(1730, 255, duration=0.2) #hosidius i inventory, cape tele. 
#     aut.click()
#     aut.moveTo(1415, 200, duration=0.2) # där du står 
#     aut.click(button="right")
#     aut.moveRel(0, 25, duration=0.2) #
#     time.sleep(3)
#     aut.click()
#     time.sleep(1)
#     time.sleep(random.uniform(620, 680))

#pl8body 190 cam
# for i in range (100):
#     aut.moveTo(1270, 282, duration=0.2) # anvil
#     aut.click()
#     time.sleep(5)

#     aut.moveTo(1345, 260, duration=0.2) # body
#     aut.click()
#     time.sleep(5)

#     time.sleep(random.uniform(14, 16))

#     aut.moveTo(1524, 127, duration=0.2) # banker
#     aut.click()
#     time.sleep(random.uniform(5, 8))


#     aut.moveTo(1775, 259, duration=0.2) # banka allt
#     aut.click()
#     time.sleep(1)


#     aut.moveTo(1339, 128, duration=0.2) #ta bars
#     aut.click()
#     time.sleep(1)

#     aut.press("esc")
#     time.sleep(0.7)



#fish chum 
# while True:
        
#     aut.moveTo(1435, 294, duration=0.2) #ta MARLINS
#     aut.click()
#     time.sleep(1)

#     aut.press("esc")
#     time.sleep(0.7)

#     aut.moveTo(1735, 290, duration=0.2) #marlin inv 
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1326, 253, duration=0.2) #chum spreader 
#     aut.click()
#     time.sleep(6)

#     aut.moveTo(1511, 193, duration=0.2) #bank
#     aut.click()
#     time.sleep(2)