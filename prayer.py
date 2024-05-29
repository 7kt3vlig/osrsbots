import pyautogui as aut
import time 
import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os

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
                time.sleep(4)
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
                aut.moveTo(x + 5 , y + 77)
                aut.click()
                time.sleep(8)
                aut.press("enter")
                time.sleep(3)
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)


def praya():
    aut.moveTo(826,125)   
    aut.click()
    time.sleep(4) 
    
    for i in range (39):
        aut.moveTo(1282, 466)
        aut.click()

        aut.moveTo(824, 192)
        aut.click()

def tbx():
    aut.moveTo(844, 319)
    aut.click()
    time.sleep(4)

def portalen():
    aut.moveTo(839, 164) #portalen 
    time.sleep(0.2)
    aut.click(button="right")
    time.sleep(0.2)
    aut.moveTo(839, 236)
    aut.click()
    time.sleep(1)
    aut.press("enter")
    time.sleep(3)

def bonesinnanphilas():
    aut.moveTo(1156, 251)  
    time.sleep(1)
    aut.click()    

portalen()

while True:
    
    praya()
    tbx()

    bonesinnanphilas()
    hittaphilas()
    hittaportalen()

