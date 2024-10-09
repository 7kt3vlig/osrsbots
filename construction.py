import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os


def larder():
    aut.moveTo(784, 194) #gå till stol platsen 
    time.sleep(0.2)
    aut.click()
    time.sleep(4)

def bygglarder(): #2 gånger per inv 

    for x in range (3):

        aut.moveTo(836, 174)
        time.sleep(0.2)
        aut.click(button="right")
        aut.moveTo(836, 224)
        time.sleep(0.2)
        aut.click()
        time.sleep(0.7)
        aut.press("2")
        time.sleep(2)


        aut.moveTo(836, 174)
        time.sleep(0.2)
        aut.click(button="right")
        aut.moveTo(836, 244)
        time.sleep(0.2)
        aut.click()
        time.sleep(0.7)
        aut.press("1")
        time.sleep(1)

def tbxlarder():
    aut.moveTo(903, 209)
    time.sleep(0.2)
    aut.click()
    time.sleep(5)
    aut.moveTo(1155, 286)
    aut.click()

def portalen():
    aut.moveTo(839, 164) #portalen 
    time.sleep(0.2)
    aut.click(button="right")
    time.sleep(0.2)
    aut.moveTo(839, 216)
    aut.click()
    time.sleep(3)

def stolen():

    aut.moveTo(814, 115) #gå till stol platsen 
    time.sleep(0.2)
    aut.click()
    time.sleep(4)


def bygg(): #11 gånger per inv 

    for x in range (3):

        aut.moveTo(825, 192)
        time.sleep(0.2)
        aut.click(button="right")
        aut.moveTo(825, 242)
        time.sleep(0.2)
        aut.click()
        time.sleep(0.7)
        aut.press("1")
        time.sleep(2)


        aut.moveTo(825, 192)
        time.sleep(0.2)
        aut.click(button="right")
        aut.moveTo(825, 259)
        time.sleep(0.2)
        aut.click()
        time.sleep(0.7)
        aut.press("1")
        time.sleep(1)

def tbx():
    aut.moveTo(886, 346)
    time.sleep(0.2)
    aut.click()
    time.sleep(5)
    aut.moveTo(1155, 286)
    aut.click()



# Define the ROI coordinates
roi_top_left = (747, 293)
roi_bottom_right = (827, 361)

def hittaphilas():
    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(roi_top_left[0],roi_top_left[1], roi_bottom_right[0], roi_bottom_right[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))
            
            # Load the template image
            template = cv.imread("philas5.png")
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("max val =", max_val)
            if max_val >= 0.4:
                
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + roi_top_left[0]
                y = max_loc[1] + roi_top_left[1]
                print(f"found the fucker at Max Value: {max_val}, Location: ({max_loc[0] + roi_top_left[0]}, {max_loc[1] + roi_top_left[1]})")
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


top_left = (751, 25)
bottom_right = (882, 140)

def hittaportalen():
    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(top_left[0],top_left[1], bottom_right[0], bottom_right[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))
            
            # Load the template image
            template = cv.imread("portalen.png")
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("max val =", max_val)
            if max_val >= 0.4:
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + top_left[0]
                y = max_loc[1] + top_left[1]
                
                aut.moveTo(x + 5 , y + 5)
                aut.click(button="right")
                aut.moveTo(x + 5 , y + 57)
                aut.click()
                time.sleep(8)
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)


portalen()

while True:
        
    larder()
    bygglarder()
    tbxlarder()
    hittaphilas()
    hittaportalen()
