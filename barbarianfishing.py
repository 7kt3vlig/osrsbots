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

    template = cv.imread(str("fullinventory.png"), cv.IMREAD_GRAYSCALE)

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




def confirmclosestfishingspot():
    top_left = 246, 231
    bottom_right = 279, 262

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str("sturgeon.png"), cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(template, grayscale, cv.TM_CCOEFF_NORMED )

    threshold = 0.76

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(min_val, max_val, min_loc, max_loc)
    
    if threshold >= max_val:
        print(max_val, max_loc)
        return True
    else:
        print(max_val, max_loc)
        return False
    


def findclosestfishingspot():

    print("Executing findclosestfishingspot()")
    top_left = 1, 227
    bottom_right = 515, 270

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str("sturgeon.png"), cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED )

    threshold = 0.8

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(min_val, max_val, min_loc, max_loc)
    locs = np.where(result >= threshold)

    best_match_loc = None
    best_distance = float('inf')

    # Target coordinates
    target_x, target_y = 263, 191

    # Iterate over all locations above threshold and find the closest one to the target coordinates
    for pt in zip(*locs[::-1]):
        center_x = pt[0] + (template.shape[1] // 2)
        center_y = pt[1] + (template.shape[0] // 2)

        distance = ((center_x - target_x) ** 2 + (center_y - target_y) ** 2) ** 0.5

        if distance < best_distance:
            best_match_loc = pt
            best_distance = distance

    if best_match_loc is not None:
        # Click at the center of the best match location in actual screen coordinates
        max_loc_screen_x = top_left[0] + best_match_loc[0] + 10
        max_loc_screen_y = top_left[1] + best_match_loc[1] + 15
        aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)
        aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)  # Click twice on the best match
    else:
        aut.scroll(-5000)
        aut.moveTo(262, 212)
        aut.click()
        time.sleep(10)


# while True:
#     confirm_result = confirmclosestfishingspot()
#     print("confirm_result:", confirm_result)
#     time.sleep(0.6)
#     if confirm_result == False:  # Check if confirmclosestfishingspot() returns False
#         findclosestfishingspot()
#         print("findclosestfishingspot() executed successfully")  # Add a debug print to confirm execution

#     fiska()
#     kolla_inventory()

findclosestfishingspot()