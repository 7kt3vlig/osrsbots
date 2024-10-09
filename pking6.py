import pyautogui as aut
import numpy as np
import cv2 as cv
from pynput.keyboard import Key, Listener
import math
import time 

# runelite 307 103 ,  1546 773
# Load template images

#mage
magecape_template = cv.imread("magecape.png")
occult_template = cv.imread("occult.png")
staff_template = cv.imread("toxicstaff.png")
ghostlyrobebottoms_template = cv.imread("ghostlyrobebottoms.png")
ahrimstaff_template = cv.imread("ahrimstaff.png")
guthixrobelegs_template = cv.imread("guthixrobelegs.png")
guthixrobetop_template = cv.imread("guthixrobetop.png")
guthixmitre_template = cv.imread("guthixmitre.png")
mysticsmokestaff_template = cv.imread("mysticsmokestaff.png")

#melee

dds_template = cv.imread("dds.png")
firecape_template = cv.imread("firecape.png")
stramulet_template = cv.imread("strammy.png")
voidwaker_template = cv.imread("voidwaker.png")
ags_template = cv.imread("ags.png")


#range

crossbow_template = cv.imread("crossbow.png")
runecrossbow_template = cv.imread("runecrossbow.png")
blackdhidechaps_template = cv.imread("blackdhidechaps.png")
dragoncbow_template = cv.imread("dragoncbow.png")
guthixchaps_template = cv.imread("guthixchaps.png")


aut.PAUSE = 0.04 # Remove any pauses between actions


def antifailspec():
    top_left = (1000, 395)
    bottom_right = (1230, 447)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("firesurge.png")
    
    if template is None:
        print("Template image antifail.png not found or unable to load.")
        return False

    # Define the threshold for a match
    threshold = 0.8

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
    print("Printing matching values for antifail:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for antifail.")
       
        return True
    else:
        print("No match found above the threshold for antifail.")
        return False

def firesurge():
    top_left = (1026, 660)
    bottom_right = (1069, 702)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("firesurge.png")
    
    if template is None:
        print("Template image firesurge.png not found or unable to load.")
        return False

    # Define the threshold for a match
    threshold = 0.8

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
    print("Printing matching values for firesurge:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for firesurge.")
       
        return True
    else:
        print("No match found above the threshold for firesurge.")
        return False


def TB():
    top_left = (1123, 630)
    bottom_right = (1165, 676)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("TB.png")
    
    if template is None:
        print("Template image tb.png not found or unable to load.")
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
    print("Printing matching values for tb:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for tb.")
       
        return True
    else:
        print("No match found above the threshold for tb.")
        return False


def entangle():
    top_left = (1155, 596)
    bottom_right = (1200, 639)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("entangle.png")
    
    if template is None:
        print("Template image entangle.png not found or unable to load.")
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
    print("Printing matching values for entangle:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for entangle.")
       
        return True
    else:
        print("No match found above the threshold for entangle.")
        return False










def meleepray():
    top_left = (1177, 487)
    bottom_right = (1237, 547)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("meleepray.png")
    
    if template is None:
        print("Template image meleepray.png not found or unable to load.")
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
    print("Printing matching values for meleepray:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for meleepray. Clicking on the position.")
       
        return True
    else:
        print("No match found above the threshold for meleepray.")
        return False
def rangepray():
    top_left = (1178, 537)
    bottom_right = (1233, 586)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("rangepray.png")
    
    if template is None:
        print("Template image rangepray.png not found or unable to load.")
        return False

    # Define the threshold for a match
    threshold = 0.6

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
    print("Printing matching values for rangepray:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for rangepray. Clicking on the position.")
       
        return True
    else:
        print("No match found above the threshold for rangepray.")
        return False
def magepray():
    top_left = (980, 586)
    bottom_right = (1047, 641)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("magepray.png")
    
    if template is None:
        print("Template image magepray.png not found or unable to load.")
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
    print("Printing matching values for magepray:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
    
    # If the match is above the threshold, click on the position
    if max_val >= threshold:
        print("Match found for magepray. Clicking on the position.")
       
        return True
    else:
        print("No match found above the threshold for mageepray.")
        return False
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
def checkrangeitems():

    area_to_check = (999, 531, 233, 185)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [
        ("runecrossbow", runecrossbow_template),
        ("sunlightcrossbow", crossbow_template),
        ("dragoncrossbow", dragoncbow_template),
        ("guthixchaps", guthixchaps_template),
        ("blackdhidechaps", blackdhidechaps_template)
        
    ]

    # Find matches in the specified area
    matches = find_matches(templates_to_check, area_to_check)
    
    if matches:
        click_matches(matches)  # Click all found items
    else:
        print("No items matched in the specified area.")

def checkmeleeitems2():
# Define the area to check (x, y, width, height)
    area_to_check = (999, 531, 233, 185)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [("staff", staff_template),
                          ("voidwaker", voidwaker_template),
                          ("ags", ags_template),
        ("firecape", firecape_template),
        ("blackdhidechaps", blackdhidechaps_template),
        ("strammy", stramulet_template)
        
        
    ]

    # Find matches in the specified area
    matches = find_matches(templates_to_check, area_to_check)
    
    if matches:
        click_matches(matches)  # Click all found items
    else:
        print("No items matched in the specified area.")



def check_mageitems():
    # Define the area to check (x, y, width, height)
    area_to_check = (999, 531, 233, 185)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [("toxicstaff", staff_template),
                          ("mysticsmokestaff", mysticsmokestaff_template),
             ("ahrimstaff", ahrimstaff_template),
        ("magecape", magecape_template),
        ("occult", occult_template),
        ("ghostlyrobebottoms", ghostlyrobebottoms_template),
        ("guthixrobetop", guthixrobetop_template),
        ("guthixrobelegs", guthixrobelegs_template),
        ("guthixmitre", guthixmitre_template)
        
        
    ]

    # Find matches in the specified area
    matches = find_matches(templates_to_check, area_to_check)
    
    if matches:
        click_matches(matches)  # Click all found items
    else:
        print("No items matched in the specified area.")


def checkmeleeitems():
# Define the area to check (x, y, width, height)
    area_to_check = (999, 531, 233, 185)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [
        ("dds", dds_template),
         ("ags", ags_template),
        ("voidwaker", voidwaker_template),
        ("firecape", firecape_template),
        ("strammy", stramulet_template),
        ("blackdhidechaps", blackdhidechaps_template)
    ]

    # Find matches in the specified area
    matches = find_matches(templates_to_check, area_to_check)
    
    if matches:
        click_matches(matches)  # Click all found items
    else:
        print("No items matched in the specified area.")



# # Target border color (RGB)
# target_color = (3, 241, 240)  # Updated to the new target color

# Function to find the red square and click in the center
def find_and_click_red_square():
   # Define the region to capture (x1, y1, width, height)
    region = (313, 135, 645, 429)  # Define your capture region here
    
    # Capture the screen in the defined region
    screenshot = aut.screenshot(region=region)
    screenshot_np = np.array(screenshot)

    # Convert the image from RGB to BGR format (OpenCV uses BGR)
    screenshot_bgr = cv.cvtColor(screenshot_np, cv.COLOR_RGB2BGR)

    # Convert BGR to HSV color space
    hsv_image = cv.cvtColor(screenshot_bgr, cv.COLOR_BGR2HSV)

    # Define the lower and upper bounds for cyan in HSV
    lower_cyan = np.array([85, 100, 100])  # Adjust saturation and value as needed
    upper_cyan = np.array([95, 255, 255])

    # Create a mask for the cyan color
    mask = cv.inRange(hsv_image, lower_cyan, upper_cyan)

    # Find contours in the masked image
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Check if any cyan shape was detected
    if len(contours) == 0:
        print("No cyan shape detected.")
        return

    # Loop through the contours and detect cyan shapes
    for contour in contours:
        # Get the bounding box coordinates for the contour
        x, y, w, h = cv.boundingRect(contour)

        # Calculate the center of the cyan shape
        center_x = x + w // 2
        center_y = y + h // 2

        # Adjust for the region offset to get absolute screen coordinates
        absolute_center_x = center_x + region[0]
        absolute_center_y = center_y + region[1]

        # Move the mouse to the center of the shape and click
        aut.moveTo(absolute_center_x, absolute_center_y)
        aut.click()

        print(f"Clicked on cyan shape at ({absolute_center_x}, {absolute_center_y})")

        return


#636 349 center own character 




target_color = (0, 255, 255)  # Updated to the new target color


def walkhere():
    # Define the region to capture (x1, y1, width, height)
    region = (313, 135, 645, 429)  # (x1, y1, width, height)
    
    # Capture the screen in the defined region
    screenshot = aut.screenshot(region=region)
    screenshot_np = np.array(screenshot)

    # Convert the image from RGB to BGR format (OpenCV uses BGR)
    screenshot_bgr = cv.cvtColor(screenshot_np, cv.COLOR_RGB2BGR)

    # Convert the image to HSV color space
    hsv_image = cv.cvtColor(screenshot_bgr, cv.COLOR_BGR2HSV)

    # Define the range for the target color in HSV
    target_hsv = cv.cvtColor(np.uint8([[target_color]]), cv.COLOR_RGB2HSV)[0][0]

    # Define a tolerance for color detection
    tolerance = 10  # Adjust this value as needed
    lower_bound = np.array([target_hsv[0] - tolerance, 100, 100])
    upper_bound = np.array([target_hsv[0] + tolerance, 255, 255])

    # Create a mask for the target color
    mask = cv.inRange(hsv_image, lower_bound, upper_bound)

    # Find contours in the masked image
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Reference point (set to 636, 349)
    reference_point = (636, 349)

    nearest_distance = float('inf')  # Start with a large number
    nearest_center = None  # Will store the nearest shape's center

    # Loop through the contours and detect shapes
    for contour in contours:
        # Approximate the contour and get the bounding box
        epsilon = 0.02 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)

        # Get the bounding box coordinates
        x, y, w, h = cv.boundingRect(approx)
        center_x, center_y = x + w // 2, y + h // 2  # Calculate the center relative to the region

        # Adjust for the region offset to get absolute coordinates
        absolute_center_x = center_x + region[0]
        absolute_center_y = center_y + region[1]

        # Calculate the distance from the reference point (636, 349) to the absolute center of the shape
        distance = math.sqrt((absolute_center_x - reference_point[0]) ** 2 + (absolute_center_y - reference_point[1]) ** 2)

        # Check if this shape is the nearest one so far
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_center = (absolute_center_x, absolute_center_y)
            print(f"Found nearer shape at ({absolute_center_x}, {absolute_center_y}) with distance {distance}")

    # If a nearest shape was found, click it
    if nearest_center is not None:
        # Move the mouse to the center and click
        aut.moveTo(nearest_center[0], nearest_center[1])
        aut.click(button="right")
        aut.moveTo(nearest_center[0], nearest_center[1] + 33)
        aut.click()
        print(f"Clicked at nearest shape at ({nearest_center[0]}, {nearest_center[1]})")
    else:
        print("No shape of the target color found.")
    







def function_e():
    aut.press("2")
    check_mageitems()  # Check for magecape, occult, and staff when 'e' is pressed
    aut.press("3") #mage pray
    if not magepray():
            aut.moveTo(1020, 615, duration=0.01)#
            aut.click()

            aut.press("4") #mage book 
            if not firesurge():
    
                aut.moveTo(1049, 681, duration=0.01)#fire surge 
                aut.click()
            
                aut.press("2") #inv 
                find_and_click_red_square()
                

    if magepray():
        aut.press("4") #mage book 
        if not firesurge():
            aut.moveTo(1049, 681, duration=0.01)#fire surge 
            aut.click()
            
            aut.press("2") #inv 
            find_and_click_red_square()
            

def function_r():
    aut.press("2")
    checkmeleeitems()

    aut.press("3") #melee pray
    if not meleepray():


        aut.moveTo(1025, 565, duration=0.01)#
        aut.click()
        
        aut.moveTo(1205, 520, duration=0.01)#
        aut.click()

        aut.press("1") #spec
        if not antifailspec():
            aut.moveTo(1100, 665, duration=0.01)#
            aut.click()
            

            aut.press("2") #inv 
            find_and_click_red_square()
        if antifailspec():
            return
        

    if meleepray():
        aut.press("1") #spec
        aut.moveTo(1100, 665, duration=0.01)#
        aut.click()


        aut.press("2") #inv 
        find_and_click_red_square()
        

def function_w():
    aut.press("2")
    checkrangeitems()
    aut.press("3") #range pray
    if not rangepray():


        aut.moveTo(1206, 565, duration=0.01)#
        aut.click()

        aut.press("2") #inv 
        find_and_click_red_square()
       

    if rangepray():
        aut.press("2") #inv 
        find_and_click_red_square()
   

def function_q():
    aut.press("2")
    checkmeleeitems2()
    aut.press("3") #melee pray
    if not meleepray():


        aut.moveTo(1025, 565, duration=0.01)#
        aut.click()
        
        aut.moveTo(1205, 520, duration=0.01)#
        aut.click()

        aut.press("2") #inv 
        find_and_click_red_square()
 

    if meleepray():
    
        aut.press("2") #inv 
        find_and_click_red_square()
 

def function_f():#entangle
    aut.press("2")
    check_mageitems()  # Check for magecape, occult, and staff when 't' is pressed
    aut.press("3") #mage pray
    if not magepray():
            aut.moveTo(1020, 615, duration=0.01)#
            aut.click()

            aut.press("4") #mage book 
            if not entangle():
        

                aut.moveTo(1180, 620, duration=0.01)#entangle
                aut.click()
                
                aut.press("2") #inv 
                find_and_click_red_square()

    if magepray():
        aut.press("4") #mage book 
        if not entangle():
            aut.moveTo(1180, 620, duration=0.01)#entangle
            aut.click()
            
            aut.press("2") #inv 
            find_and_click_red_square()
        
def function_t():#tb
    aut.press("2")
    check_mageitems()  # Check for magecape, occult, and staff when 't' is pressed
    aut.press("3") #mage pray
    if not magepray():
            aut.moveTo(1020, 615, duration=0.01)#
            aut.click()

            aut.press("4") #mage book 
            if not TB():
        

                aut.moveTo(1146, 650, duration=0.01)#TB
                aut.click()
                
                aut.press("2") #inv 
                find_and_click_red_square()

    if magepray():
        aut.press("4") #mage book 
        if not TB():
            aut.moveTo(1146, 650, duration=0.01)#TB
            aut.click()
            
            aut.press("2") #inv 
            find_and_click_red_square()


def function_5():
    walkhere()


# Listener functions
def on_press(key):
    try:
        # Check if specific keys are pressed and execute respective functions
        if key.char == 'e':
            function_e()
        elif key.char == 'r':
            function_r()
        elif key.char == 'w':
            function_w()
        elif key.char == 'q':
            function_q()
        elif key.char == 't':
            function_t()
        elif key.char == 'f':
            function_f()
        elif key.char == '5':
            function_5()
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


#gör en nödknapp som slutar switcha om du tryckt fel 