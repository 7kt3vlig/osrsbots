import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 


def fiska():

    aut.moveTo(364, 249)
    aut.click()

def droppa():
    
    aut.keyDown("shift")
#rad1
    aut.moveTo(666, 259)
    aut.click()

    aut.moveTo(666, 295)
    aut.click()

    aut.moveTo(666, 330)
    aut.click()

    aut.moveTo(666, 367)
    aut.click()

    aut.moveTo(666, 404)
    aut.click()

    aut.moveTo(666, 440)
    aut.click()

    aut.moveTo(666, 475)
    aut.click()
#rad 2 
    
    aut.moveTo(708, 259)
    aut.click()

    aut.moveTo(708, 295)
    aut.click()

    aut.moveTo(708, 330)
    aut.click()

    aut.moveTo(708, 367)
    aut.click()

    aut.moveTo(708, 404)
    aut.click()

    aut.moveTo(708, 440)
    aut.click()

    aut.moveTo(708, 475)
    aut.click()

    #rad 3

    aut.moveTo(623, 295)
    aut.click()

    aut.moveTo(623, 330)
    aut.click()

    aut.moveTo(623, 367)
    aut.click()

    aut.moveTo(623, 404)
    aut.click()

    aut.moveTo(623, 440)
    aut.click()

    aut.moveTo(623, 475)
    aut.click()
#rad 4
    aut.moveTo(579, 295)
    aut.click()

    aut.moveTo(579, 330)
    aut.click()

    aut.moveTo(579, 367)
    aut.click()

    aut.moveTo(579, 404)
    aut.click()

    aut.moveTo(579, 440)
    aut.click()

    aut.moveTo(579, 475)
    aut.click()


def kollainventory():

    try:
        screenshot = ImageGrab.grab(bbox=(10, 370, 521, 507))#847, 214, 861, 228)
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        
        # Load the template image
        template = cv.imread("fullinv.png")
        
        # Perform template matching
        result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    except Exception as e:
        print("Error:", e)
    finally:
        try:
            os.remove("sample.png")
            print("File 'sample.png' removed successfully.")
        except Exception as e:
            print("Error while removing file:", e)
        if max_val >= 0.6:
            droppa()
        else:
            pass


def kollafiskstatus():
    try:
        screenshot = ImageGrab.grab(bbox=(56, 56, 140, 75))#847, 214, 861, 228)
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        
        # Load the template image
        template = cv.imread("status.png")
        
        # Perform template matching
        result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    except Exception as e:
        print("Error:", e)
    finally:
        try:
            os.remove("sample.png")
            print("File 'sample.png' removed successfully.")
        except Exception as e:
            print("Error while removing file:", e)
        if max_val >= 0.9:
            pass
        else:
            fiska()


'''
droppa
fiska 
kolla inventory 
kollafiska 

1 kolla inventory - om ej full - kollafiskastatus - annars droppa - 

2 kollafiska - om ej fiska - fiska - annars låt gå(pas s)
'''
while True:

    kollainventory()
    kollafiskstatus()