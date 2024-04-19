import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 

print("checking dodgyneck..")

# Define the region of interest (ROI) coordinates
roi_top_left = (9, 32)
roi_bottom_right = (520, 366)

# Define a list of template image filenames
template_filenames = ["paladin.png", "paladin1.png", "paladin2.png", "paladin3.png"]

while True:
    for template_filename in template_filenames:
        screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                            roi_bottom_right[0] - roi_top_left[0], 
                                            roi_bottom_right[1] - roi_top_left[1]))

        # Convert the screenshot to OpenCV format (BGR)
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

        # Convert the filtered image to grayscale
        grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

        # Load the template image
        template = cv.imread(template_filename, cv.IMREAD_GRAYSCALE)

        # Blur both the grayscale image and the template
        blur = cv.blur(grayscale_img, (3,3))
        blur1 = cv.blur(template, (3,3))

        # Apply Canny edge detection to both images
        canny = cv.Canny(blur, 125, 175)
        canny1 = cv.Canny(blur1, 125, 175)

        # Perform template matching
        result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

        # Define a threshold for the match
        threshold = 0.2

        # Get the location of the best match
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # Calculate the center of the max location
        template_height, template_width = template.shape
        center_x = max_loc[0] + template_width // 2
        center_y = max_loc[1] + template_height // 2

        # Convert the center coordinates to the actual screen location
        center_screen = (center_x + roi_top_left[0], center_y + roi_top_left[1])

        # Print the template filename, maximum value, and its center screen location
        print("Template:", template_filename)
        print("Max value:", max_val)
        print("Max center location (on screen):", center_screen)
        print()

        # If the maximum value exceeds the threshold, click 18 pixels to the right and 29 pixels down from the center screen location
        if max_val >= threshold:
            aut.click(center_screen[0] + 18, center_screen[1] + 29)

        # Add a short delay before moving to the next template
        time.sleep(1)