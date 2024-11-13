import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 

#camera zoom 293
#starting position höger sida bank

def movetofarmer():
        
    aut.moveTo(651, 82)
    aut.click()
    time.sleep(20)

def buy_pots():
    aut.moveTo(425, 115)
    aut.click()
    aut.press("esc")

def hop_world():
    # Define a static variable to keep track of the counter
    if not hasattr(hop_world, 'counter'):
        hop_world.counter = 531

    # Move to the target location
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop {}".format(hop_world.counter))
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()

    # Increment the counter
    hop_world.counter += 1

    # Reset the counter to 531 if it exceeds 535
    if hop_world.counter > 535:
        hop_world.counter = 531

# def detect_farmer():
#     print("detecting farmer..")
#     aut.moveTo(680, 511)
#     aut.click()
#     time.sleep(0.6)
#     aut.moveTo(660, 346)
#     aut.click()
#     aut.moveTo(650, 210)
#     aut.click()
#     condition_met = False
#     while not condition_met:
# # Define the region of interest (ROI) coordinates
#         roi_top_left = (8, 34)
#         roi_bottom_right = (516, 364)
#         # Scale the ROI coordinates to screen resolution
      
#         screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
#                                             roi_bottom_right[0] - roi_top_left[0], 
#                                             roi_bottom_right[1] - roi_top_left[1]))

#         # Convert the screenshot to OpenCV format (BGR)
#         screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


#         # Convert the filtered image to grayscale
#         grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

#         # Load the template image
#         template1 = cv.imread('farmer.png', cv.IMREAD_GRAYSCALE)
#         template2 = cv.imread('farmer2.png', cv.IMREAD_GRAYSCALE)
#         template3 = cv.imread('farmer3.png', cv.IMREAD_GRAYSCALE)
#         template4 = cv.imread('farmer4.png', cv.IMREAD_GRAYSCALE)
#         template5 = cv.imread('farmer5.png', cv.IMREAD_GRAYSCALE)
#         template6 = cv.imread('farmer6.png', cv.IMREAD_GRAYSCALE)

#         templates = [template1, template2, template3, template4, template5, template6]
        
#         # Blur both the grayscale image and the template
#         blur = cv.blur(grayscale_img, (3,3))
#         # blur1 = cv.blur(template1, (3,3))

#         # Apply Canny edge detection to both images
#         canny = cv.Canny(blur, 125, 175)
#         # canny1 = cv.Canny(blur1, 125, 175)
#         # cv.imshow("1", canny)
#         # cv.imshow("2", canny1)
#         # cv.waitKey(0)
#         # cv.destroyAllWindows
        
#             # Apply template matching
#         # result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)
#         for template in templates:
#     # Blur the template
#             blur_template = cv.blur(template, (3, 3))
            
#             # Apply Canny edge detection to the template
#             canny_template = cv.Canny(blur_template, 125, 175)
            
#             # Apply template matching
#             result = cv.matchTemplate(canny, canny_template, cv.TM_CCOEFF_NORMED)
            
#     # Process the result as needed
#     # For example, find the location of the best match
#             min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


#             # Define a threshold for the match
#             threshold = 0.45


#             # Get the location of the best match
#     # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

#             # Check if the maximum match value is above the threshold
#             if max_val >= threshold:
#                     print("Match found!")
#                     # Convert the coordinates to real screen coordinates
#                     match_center_x = max_loc[0] + template.shape[1] // 2 + roi_top_left[0]
#                     match_center_y = max_loc[1] + template.shape[0] // 2 + roi_top_left[1]
                
#                     aut.click(match_center_x, match_center_y,)
#                     time.sleep(5)
#                     condition_met = True
#                     pass
#             else:
#                     print("Template not found in the screenshot")
def detect_farmer():
   # Define the region to capture (x1, y1, width, height)
    region = (8, 34, 515, 336)  # Define your capture region here
    
    # Target coordinates (to find the closest shape to these)
    target_x = 266
    target_y = 194

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
        if w < 6 or h < 6:
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
        time.sleep(3)
        print(f"Clicked on the closest cyan shape at {closest_center} with a distance of {closest_distance:.2f}")
    else:
        print("No valid cyan shapes were found to click on.")

def detect_bank():
    print("detecting bank..")
    condition_met = False
    while not condition_met:
# Define the region of interest (ROI) coordinates
        roi_top_left = (575, 37)
        roi_bottom_right = (717, 169)
        screen_width, screen_height = aut.size()

        # Scale the ROI coordinates to screen resolution
        roi_top_left_scaled = (int(roi_top_left[0] * screen_width / 1920), int(roi_top_left[1] * screen_height / 1080))
        roi_bottom_right_scaled = (int(roi_bottom_right[0] * screen_width / 1920), int(roi_bottom_right[1] * screen_height / 1080))

        screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                            roi_bottom_right[0] - roi_top_left[0], 
                                            roi_bottom_right[1] - roi_top_left[1]))

        # Convert the screenshot to OpenCV format (BGR)
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


        # Convert the filtered image to grayscale
        grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

        # Load the template image
        template1 = cv.imread('bankikon.png', cv.IMREAD_GRAYSCALE)

        # Blur both the grayscale image and the template
        blur = cv.blur(grayscale_img, (3,3))
        blur1 = cv.blur(template1, (3,3))

        # Apply Canny edge detection to both images
        canny = cv.Canny(blur, 125, 175)
        canny1 = cv.Canny(blur1, 125, 175)
        # cv.imshow("1", canny)
        # cv.imshow("2", canny1)
        # cv.waitKey(0)
        # cv.destroyAllWindows
            # Apply template matching
        result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

            # Define a threshold for the match
        threshold = 0.6

            # Get the location of the best match
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

            # Check if the maximum match value is above the threshold
        if max_val >= threshold:
        # Calculate the center coordinates of the match
            match_width, match_height = template1.shape[::-1]
            center_x = max_loc[0] + match_width // 2
            center_y = max_loc[1] + match_height // 2

            # Convert the matched location to global screen coordinates
            global_center_x = center_x + roi_top_left_scaled[0]
            global_center_y = center_y + roi_top_left_scaled[1]

            # Click at the center of the match
            aut.click(global_center_x, global_center_y)
            time.sleep(0.1)
            aut.click(global_center_x, global_center_y)
            time.sleep(20)
            print(max_val, (center_x, center_y))
            condition_met = True
                
        else:
                print("Template not found")
                print(max_val, max_loc)

def detect_banker():
    print("detecting banker..")
    region = (8, 34, 515, 336)  # Define your capture region here
    
    # Target coordinates (to find the closest shape to these)
    target_x = 266
    target_y = 194

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
        if w < 6 or h < 6:
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
        time.sleep(3)
        print(f"Clicked on the closest cyan shape at {closest_center} with a distance of {closest_distance:.2f}")
    else:
        print("No valid cyan shapes were found to click on.")

# def resize():
#     aut.moveTo(680, 511)
#     aut.click()
#     time.sleep(0.6)
#     aut.moveTo(660, 346)
#     aut.click()
#     aut.moveTo(627, 345)
#     aut.click()

def bank():
    aut.moveTo(625, 265)#bagged pots
    aut.click()
    time.sleep(1)
    aut.press("esc")
def bank2():

    aut.moveTo(625, 265)#bagged pots
    aut.click()
    time.sleep(1)
    aut.moveTo(164, 91)
    aut.click()
    time.sleep(1)
    aut.moveTo(90, 315)
    aut.click()
    time.sleep(1)
    aut.press("esc")
    aut.moveTo(626, 264)
    aut.click()
    time.sleep(0.6)
    detect_banker()
    aut.moveTo(625, 265)
    aut.click()
    time.sleep(1)
    aut.press("esc")


while True:
        




    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 506")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()



    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 507")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()



    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 508")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()



    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 509")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()



    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 510")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()


    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 511")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()



    












    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 512")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()







    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 513")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()










    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 514")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()












    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 515")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()












    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 516")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()













    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 517")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()
















    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank2()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 518")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()



    movetofarmer()
    detect_farmer()
    buy_pots()
    detect_bank()
    detect_banker()
    bank()
    aut.moveTo(430, 440)
    aut.click()
    aut.press("enter")
    time.sleep(0.6)

    # Write the current hop number
    aut.write("::hop 519")
    time.sleep(0.6)
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()