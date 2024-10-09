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
        pause()
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
    time.sleep(0.4)

    
    aut.moveTo(263, 248)
    aut.click()
    time.sleep(0.8)




def findfishingspot():
    print("Executing findclosestfishingspot()")
    top_left = 1, 215
    bottom_right = 515, 260

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
    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

    threshold = 0.6

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print("Min val:", min_val)
    print("Max val:", max_val)
    print("Min loc:", min_loc)
    print("Max loc:", max_loc)
    


    if max_val >= threshold:
        locs = np.where(result >= threshold)

        best_match_val = -float('inf')
        best_match_loc = None

        # Iterate over all locations above threshold and find the one with the highest match value
        for pt in zip(*locs[::-1]):
            if result[pt[::-1]] > best_match_val:
                best_match_val = result[pt[::-1]]
                best_match_loc = pt

        if best_match_loc is not None:
            # Click at the center of the best match location in actual screen coordinates
            max_loc_screen_x = top_left[0] + best_match_loc[0] + 12
            max_loc_screen_y = top_left[1] + best_match_loc[1] + 17
            aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)
            aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)
        else:
            print("No suitable match found. Performing default action.")
            
    else:
        print("Max value not above threshold. Performing default action.")
        
    

def confirmclosestfishingspot():
    top_left = 246, 217
    bottom_right = 279, 255

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
    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)
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
        print("spot not found!")
        print(max_val, max_loc)
        findfishingspot()
        time.sleep(4)
        
    else:
        print("spot found.")
        print(max_val, max_loc)
        fiska()


def pause():
    min_seconds = 2  # minimum number of seconds
    max_seconds = 4  # maximum number of seconds

# Generate a random float between min_seconds and max_seconds
    random_pause = random.uniform(min_seconds, max_seconds)

    # Pause execution for the random amount of time
    print(f"Pausing for {random_pause:.2f} seconds...")
    time.sleep(random_pause)
    print("Resuming execution.")

while True:
    kolla_inventory()
    confirmclosestfishingspot()
    time.sleep(0.6)
    kolla_inventory()
    