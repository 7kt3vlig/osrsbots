import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 

def kolla_inventory():
    top_left = 100, 400
    bottom_right = 390, 490

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread("fullinventory.png", cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED )

    threshold = 0.8

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("printing inventory values..")
    print(min_val, max_val, min_loc, max_loc)

    if max_val >= threshold:
        drop()
    else:
        return False


def drop():
    
    
    
    aut.moveTo(709,257)
    aut.click()
    aut.moveTo(709,293)
    aut.click()
    aut.moveTo(709,329)
    aut.click()
    aut.moveTo(709,365)
    aut.click()
    aut.moveTo(709,402)
    aut.click()
    aut.moveTo(709,438)
    aut.click()
    aut.moveTo(709,474)
    aut.click()

    aut.moveTo(666,293)
    aut.click()
    aut.moveTo(666,329)
    aut.click()
    aut.moveTo(666,365)
    aut.click()
    aut.moveTo(666,402)
    aut.click()
    aut.moveTo(666,438)
    aut.click()
    aut.moveTo(666,474)
    aut.click()
    
    
    aut.moveTo(624,329)
    aut.click()
    aut.moveTo(624,365)
    aut.click()
    aut.moveTo(624,402)
    aut.click()
    aut.moveTo(624,438)
    aut.click()
    aut.moveTo(624,474)
    aut.click()
    

    aut.moveTo(582,329)
    aut.click()
    aut.moveTo(582,365)
    aut.click()
    aut.moveTo(582,402)
    aut.click()
    aut.moveTo(582,438)
    aut.click()
    aut.moveTo(582,474)
    aut.click()
    


def fiska():
    aut.moveTo(582,256)
    aut.click()
    aut.moveTo(582,296)
    aut.click()
    time.sleep(0.6)

    aut.moveTo(263, 248)
    aut.click()
    time.sleep(0.6)




def findclosestfishingspot():
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

def confirmclosestfishingspot():
    top_left = 246, 228
    bottom_right = 279, 262

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread("sturgeon.png", cv.IMREAD_GRAYSCALE)

    blur = cv.GaussianBlur(grayscale, (3,3), 0)
    blur1 = cv.GaussianBlur(template, (3,3), 0)
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)
    result = cv.matchTemplate(blur, blur1, cv.TM_CCOEFF_NORMED)
    threshold = 0.3

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print("Min val:", min_val)
    print("Max val:", max_val)
    print("Min loc:", min_loc)
    print("Max loc:", max_loc)

    # Display grayscale image
    # cv.imshow("1", canny)
    # cv.imshow("2", canny1)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # Print template matching result
    if max_val < threshold:
        print("Template not found!")
        print(max_val, max_loc)
        return False
    else:
        print("Template found.")
        print(max_val, max_loc)
        return True


# if not confirmclosestfishingspot:      
#     findclosestfishingspot()

findclosestfishingspot()
