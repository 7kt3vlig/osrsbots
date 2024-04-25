import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 

def perform_template_matching():
    print("Executing findclosestfishingspot()")
    top_left = 1, 225
    bottom_right = 515, 259

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1]))

    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread("sturgeon.png", cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.6

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(min_val, max_val, min_loc, max_loc)

    if max_val >= threshold:
        locs = np.where(result >= threshold)

        best_match_loc = None
        best_distance = float('inf')

        matched_locations = []  # List to store all matched locations

        # Target coordinates
        target_x, target_y = 263, 191

        # Iterate over all locations above threshold and find the closest one to the target coordinates
        for pt in zip(*locs[::-1]):
            center_x = pt[0] + (template.shape[1] // 2)
            center_y = pt[1] + (template.shape[0] // 2)

            distance = ((center_x - target_x) ** 2 + (center_y - target_y) ** 2) ** 0.5

            # Check if this match is closer than the previous best match and not overlapping with it
            if distance < best_distance:
                overlapping = False
                for existing_loc in matched_locations:
                    existing_center_x = existing_loc[0] + (template.shape[1] // 2)
                    existing_center_y = existing_loc[1] + (template.shape[0] // 2)
                    existing_distance = ((existing_center_x - center_x) ** 2 + (existing_center_y - center_y) ** 2) ** 0.5
                    if existing_distance < 10:  # Adjust this threshold value as needed
                        overlapping = True
                        break
                if not overlapping:
                    best_match_loc = pt
                    best_distance = distance
                    matched_locations.append(pt)  # Append the current match to the list

        # Print all matched locations
        print("Matched Locations:")
        for match_loc in matched_locations:
            print(match_loc)

        if best_match_loc is not None:
            # Click at the center of the best match location in actual screen coordinates
            max_loc_screen_x = top_left[0] + best_match_loc[0] + 10
            max_loc_screen_y = top_left[1] + best_match_loc[1] + 15
            aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)
            aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)  # Click twice on the best match
        else:
            print("No suitable match found. Performing default action.")
            
            aut.moveTo(262, 212)
            aut.click()
            time.sleep(10)
    else:
        print("Max value not above threshold. Performing default action.")

        aut.moveTo(262, 212)
        aut.click()
        time.sleep(10)
# Call the function to perform template matching
perform_template_matching()

        # cv.waitKey(0)
        # cv.destroyAllWindows()
