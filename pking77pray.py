import pyautogui as aut
import numpy as np
import cv2 as cv
from pynput.keyboard import Key, Listener
import math
import time 

# runelite, skärm 307 103 ,  1382 771
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
bloodbarklegs_template = cv.imread("bloodbarklegs.png")
bloodbarkbody_template = cv.imread("bloodbarkbody.png")
voidmagehelm_template = cv.imread("voidmagehelm.png")
tome_template = cv.imread("tome.png")


#melee

dds_template = cv.imread("dds.png")
firecape_template = cv.imread("firecape.png")
stramulet_template = cv.imread("strammy.png")
voidwaker_template = cv.imread("voidwaker.png")
ags_template = cv.imread("ags.png")
leafbaxe_template = cv.imread("leafbaxe.png")
zombieaxe_template = cv.imread("zombieaxe.png")
ddefender_template = cv.imread("ddefender.png")
avernicdefender_template = cv.imread("avernicdefender.png")
voidhelm_template = cv.imread("voidhelm.png")


#range

crossbow_template = cv.imread("crossbow.png")
runecrossbow_template = cv.imread("runecrossbow.png")
blackdhidechaps_template = cv.imread("blackdhidechaps.png")
dragoncbow_template = cv.imread("dragoncbow.png")
guthixchaps_template = cv.imread("guthixchaps.png")
lightballista_template = cv.imread("lightballista.png")
mixedhidelegs_template = cv.imread("mixedhidelegs.png")
mixedhidetop_template = cv.imread("mixedhidetop.png")
heavyballista_template = cv.imread("heavyballista.png")
voidragnehelm_template = cv.imread("voidrangehelm.png")


#extras

antifailspec_template = cv.imread("antifailspec.png")
antifailspec1_template = cv.imread("antifailspec1.png")
antifailspec2_template = cv.imread("antifailspec2.png")
antifailspec3_template = cv.imread("antifailspec3.png")
antifailspec4_template = cv.imread("antifailspec4.png")



aut.PAUSE = 0.04 # Remove any pauses between actions


def antifailspec():
    top_left = (1031, 301)
    bottom_right = (1066, 339)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    templates = [
        cv.imread("antifailspec.png"),
        cv.imread("antifailspec1.png"),
        cv.imread("antifailspec2.png"),
        cv.imread("antifailspec3.png"),
        cv.imread("antifailspec4.png")
    ]
    
      # Check if all template images are successfully loaded
    for i, template in enumerate(templates):
        if template is None:
            print(f"Template image antifailspec{i}.png not found or unable to load.")
            return False
    
    # Define the threshold for a match
    threshold = 0.85

    # Capture the screenshot of the specified region using pyautogui
    try:
        screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                            bottom_right[0] - top_left[0],
                                            bottom_right[1] - top_left[1]))
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Check each template for a match
    for i, template in enumerate(templates):
        # Perform template matching using the color image
        result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
        
        # Get the best match position
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(f"Matching values for antifailspec{i}:")
        print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
        
        # If the match is above the threshold, return True
        if max_val >= threshold:
            print(f"Match found for antifailspec{i} with confidence {max_val}.")
            return True

    # If no match found above the threshold, return False
    print("No match found above the threshold for any antifail template.")
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
    top_left = (1035, 633)
    bottom_right = (1097, 690)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("piety.png")
    
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
    top_left = (1087, 632)
    bottom_right = (1143, 689)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image in BGR color
    template = cv.imread("rigour.png")
    
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
        print("Match found for rangepray.")
       
        return True
    else:
        print("No match found above the threshold for rangepray.")
        return False
def magepray():
    top_left = (1132, 632)
    bottom_right = (1196, 694)
    
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

    area_to_check = (999, 412, 238, 358)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [("lightballista", lightballista_template),
                          ("heavyballista", heavyballista_template),
        ("runecrossbow", runecrossbow_template),
        ("voidrangehelm", voidragnehelm_template),

        ("mixedhidetop", mixedhidetop_template),
        ("micedhidelegs", mixedhidelegs_template),
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
    area_to_check = (999, 412, 238, 358)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [("staff", staff_template),
                          ("voidwaker", voidwaker_template),
                          ("ags", ags_template),
                          ("leafbaxe", leafbaxe_template),
                          ("zombieaxe", zombieaxe_template),
                          ("voidhelm", voidhelm_template),
                          ("ddefender", ddefender_template),
                        ("avernicdefender", avernicdefender_template),

        ("firecape", firecape_template),
        ("mixedhidetop", mixedhidetop_template),
        ("micedhidelegs", mixedhidelegs_template),

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
    area_to_check = (999, 412, 238, 358)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [("toxicstaff", staff_template),
                          ("mysticsmokestaff", mysticsmokestaff_template),
             ("ahrimstaff", ahrimstaff_template),
             ("voidmagehelm", voidmagehelm_template),
             ("tome", tome_template),
        ("magecape", magecape_template),
        ("bloodbarklegs", bloodbarklegs_template),
        ("bloodbarkbody", bloodbarkbody_template),

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
    area_to_check = (999, 412, 238, 358)  # Area from (999, 533) to (1119, 629)

    # List of templates to check
    templates_to_check = [
        ("dds", dds_template),
         ("ags", ags_template),
        ("voidwaker", voidwaker_template),
        ("voidhelm", voidhelm_template),
        ("ddefender", ddefender_template),
        ("avernicdefender", avernicdefender_template),
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
                print(f"Contour {i}: Large shape detected but not a line (aspect ratio {aspect_ratio:.2f}).")

    # If a closest center was found, click on it
    if closest_center is not None:
        aut.moveTo(closest_center[0], closest_center[1])
        aut.click()
        print(f"Clicked on the closest cyan shape at {closest_center} with a distance of {closest_distance:.2f}")
    else:
        print("No valid cyan shapes were found to click on.")

# lär dig om debugging 


    






























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
            aut.moveTo(1160, 665)#augury
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


        aut.moveTo(1070, 660)#
        aut.click()
        
        

        aut.press("1") #spec
        if not antifailspec():
            
            aut.moveTo(1100, 665)#
            aut.click()
                

            aut.press("2") #inv 
            find_and_click_red_square()
            
        

    if meleepray():
        aut.press("1") #spec
        if not antifailspec():
            aut.moveTo(1100, 665)#
            
            aut.click()


            aut.press("2") #inv 
            find_and_click_red_square()
            

def function_w():
    aut.press("2")
    checkrangeitems()
    aut.press("3") #range pray
    if not rangepray():


        aut.moveTo(1115, 660)#
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


        aut.moveTo(1070, 659)#piety
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
            aut.moveTo(1160, 665)#
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
            aut.moveTo(1160, 665)#
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

def function_g():
    aut.press("space")
    aut.moveTo(1220, 700)
    aut.click()





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
        elif key.char == 'g':
            function_g()
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