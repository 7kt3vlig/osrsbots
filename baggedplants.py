import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 



def movetofarmer():
        
    aut.moveTo(651, 82)
    aut.click()
    time.sleep(30)

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

    # Write the current hop number
    aut.write("::hop {}".format(hop_world.counter))
    aut.press("enter")
    time.sleep(8)
    aut.moveTo(647, 213)
    aut.click()

    # Increment the counter
    hop_world.counter += 1

    # Reset the counter to 531 if it exceeds 535
    if hop_world.counter > 535:
        hop_world.counter = 531

def detect_farmer():
    print("detecting farmer..")
    aut.moveTo(680, 511)
    aut.click()
    time.sleep(0.6)
    aut.moveTo(660, 346)
    aut.click()
    aut.moveTo(650, 210)
    aut.click()
    condition_met = False
    while not condition_met:
# Define the region of interest (ROI) coordinates
        roi_top_left = (8, 34)
        roi_bottom_right = (516, 364)
        # Scale the ROI coordinates to screen resolution
      
        screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                            roi_bottom_right[0] - roi_top_left[0], 
                                            roi_bottom_right[1] - roi_top_left[1]))

        # Convert the screenshot to OpenCV format (BGR)
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


        # Convert the filtered image to grayscale
        grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

        # Load the template image
        template1 = cv.imread('farmer.png', cv.IMREAD_GRAYSCALE)
        template2 = cv.imread('farmer2.png', cv.IMREAD_GRAYSCALE)
        template3 = cv.imread('farmer3.png', cv.IMREAD_GRAYSCALE)
        template4 = cv.imread('farmer4.png', cv.IMREAD_GRAYSCALE)
        template5 = cv.imread('farmer5.png', cv.IMREAD_GRAYSCALE)
        template6 = cv.imread('farmer6.png', cv.IMREAD_GRAYSCALE)

        templates = [template1, template2, template3, template4, template5, template6]
        
        # Blur both the grayscale image and the template
        blur = cv.blur(grayscale_img, (3,3))
        # blur1 = cv.blur(template1, (3,3))

        # Apply Canny edge detection to both images
        canny = cv.Canny(blur, 125, 175)
        # canny1 = cv.Canny(blur1, 125, 175)
        # cv.imshow("1", canny)
        # cv.imshow("2", canny1)
        # cv.waitKey(0)
        # cv.destroyAllWindows
        
            # Apply template matching
        # result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)
        for template in templates:
    # Blur the template
            blur_template = cv.blur(template, (3, 3))
            
            # Apply Canny edge detection to the template
            canny_template = cv.Canny(blur_template, 125, 175)
            
            # Apply template matching
            result = cv.matchTemplate(canny, canny_template, cv.TM_CCOEFF_NORMED)
            
    # Process the result as needed
    # For example, find the location of the best match
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


            # Define a threshold for the match
            threshold = 0.45


            # Get the location of the best match
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

            # Check if the maximum match value is above the threshold
            if max_val >= threshold:
                    print("Match found!")
                    # Convert the coordinates to real screen coordinates
                    match_center_x = max_loc[0] + template.shape[1] // 2 + roi_top_left[0]
                    match_center_y = max_loc[1] + template.shape[0] // 2 + roi_top_left[1]
                
                    aut.click(match_center_x, match_center_y,)
                    time.sleep(5)
                    condition_met = True
                    pass
            else:
                    print("Template not found in the screenshot")

def detect_bank():
    print("detecting bank..")
    condition_met = False
    while not condition_met:
# Define the region of interest (ROI) coordinates
        roi_top_left = (620, 130)
        roi_bottom_right = (682, 158)
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
        threshold = 0.8

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
            time.sleep(30)
            print(max_val, (center_x, center_y))
            condition_met = True
                
        else:
                print("Template not found")
                print(max_val, max_loc)

def detect_banker():
    print("detecting banker..")
    condition_met = False
    while not condition_met:
# Define the region of interest (ROI) coordinates
        roi_top_left = (7, 31)
        roi_bottom_right = (519, 364)
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
        template1 = cv.imread('banker.png', cv.IMREAD_GRAYSCALE)

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
        result = cv.matchTemplate(grayscale_img, template1, cv.TM_CCOEFF_NORMED)

                # Define a threshold for the match
        threshold = 0.7

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
                time.sleep(5)
                print(max_val, max_loc, global_center_x, global_center_y)
                aut.moveTo(242, 92) #rätt tab
                aut.click()
                aut.moveTo(450, 345) #banka allt
                aut.click()
                time.sleep(0.6)
                aut.moveTo(140, 130) #ta cash 
                aut.click()
                time.sleep(1)
                aut.press("esc")
                condition_met = True
                
        else:
                    print("bankers not found")
                    print(max_val, max_loc)

def resize():
    aut.moveTo(680, 511)
    aut.click()
    time.sleep(0.6)
    aut.moveTo(660, 346)
    aut.click()
    aut.moveTo(627, 345)
    aut.click()

# while True:
        
#     movetofarmer()
#     detect_farmer()
#     buy_pots()
#     detect_bank()
#     resize()
#     detect_banker()
#     hop_world()
detect_farmer()