import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random




    # Define the ROI coordinates
roi_top_left = (580, 80)
roi_bottom_right = (1078, 327)


def hittapaladin():


    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(roi_top_left[0],roi_top_left[1], roi_bottom_right[0], roi_bottom_right[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))
            
            # Load the template image
            template = cv.imread("paladin.png")
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("max val =", max_val)
            if max_val >= 0.1:
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + roi_top_left[0]
                y = max_loc[1] + roi_top_left[1]
                
                aut.moveTo(x + 5 , y + 10)
                aut.click()
                time.sleep(8)
                aut.press("3")
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)

screenshot = ImageGrab.grab(bbox=(roi_top_left[0],roi_top_left[1], roi_bottom_right[0], roi_bottom_right[1] ))#847, 214, 861, 228)
screenshot.save("sample.png")

screenshot = np.array(Image.open("sample.png"))