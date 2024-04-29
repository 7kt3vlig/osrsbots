import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 

def perform_template_matching():
    print("Executing findclosestfishingspot()")
    top_left = 246, 217
    bottom_right = 279, 255

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1]))

    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread("sturgeon.png", cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED)

    threshold = 0.6

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print("Min val:", min_val)
    print("Max val:", max_val)
    print("Min loc:", min_loc)
    print("Max loc:", max_loc)
    
    blur = cv.GaussianBlur(grayscale, (3,3), 0)
    blur1 = cv.GaussianBlur(template, (3,3), 0)
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)
    cv.imshow("1", canny)
    cv.imshow("2", canny1)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # if max_val >= threshold:
    #     locs = np.where(result >= threshold)

    #     best_match_val = -float('inf')
    #     best_match_loc = None

    #     # Iterate over all locations above threshold and find the one with the highest match value
    #     for pt in zip(*locs[::-1]):
    #         if result[pt[::-1]] > best_match_val:
    #             best_match_val = result[pt[::-1]]
    #             best_match_loc = pt

    #     if best_match_loc is not None:
    #         # Click at the center of the best match location in actual screen coordinates
    #         max_loc_screen_x = top_left[0] + best_match_loc[0] + 10
    #         max_loc_screen_y = top_left[1] + best_match_loc[1] + 15
    #         aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)
    #         aut.click(max_loc_screen_x, max_loc_screen_y, clicks=2)  # Click twice on the best match
    #     else:
    #         print("No suitable match found. Performing default action.")
    #         aut.moveTo(262, 212)
    #         aut.click()
    #         time.sleep(10)
    # else:
    #     print("Max value not above threshold. Performing default action.")
    #     aut.moveTo(262, 212)
    #     aut.click()
    #     time.sleep(10)



perform_template_matching()


    