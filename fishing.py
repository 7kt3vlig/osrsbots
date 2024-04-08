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
    aut.moveTo(650, 212)
    aut.click()
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
    
    aut.keyUp("shift")


def kollainventory():
    print("Kollar om inventoryn e full")

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
            print("inventoryn e full")
            droppa()
        else:
            print("invenotryn e inte full")
            pass


def kollafiskstatus():
    print("kollar om vi fiskar")
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
            print("vi fiskar ")
            pass
        else:
            print("vi fiskar inte.. dags att fiska ")
            fiska()
            
def kollavartvie():
    print("kollar fiskespots") 
    screenshot = ImageGrab.grab(bbox=(313, 85, 350, 130))#847, 214, 861, 228)
    screenshot.save("sample.png")
    screenshot.close()
    screenshot = np.array(Image.open("sample.png"))
        
        # Load the template image
    template = cv.imread("fisk.png")
        
        # Perform template matching
    result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    
    
    os.remove("sample.png")
    print("File 'sample.png' removed successfully.")
        
    if max_val >= 0.12:
        print("fiskespot norra finns")
        aut.moveTo(275, 204)
        aut.click()
        time.sleep(8)
    elif max_val <= 0.12 :
        print("norra sidan finns ej, kollar sodra")
        screenshot = ImageGrab.grab(bbox=(240, 160, 280, 205))#847, 214, 861, 228)
    screenshot.save("sample.png")
    screenshot.close()
    screenshot = np.array(Image.open("sample.png"))
    
    # Load the template image
    template = cv.imread("fisk.png")
    
    # Perform template matching
    result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    os.remove("sample.png")
    print("File 'sample.png' removed successfully.")

    if max_val >= 0.12:
        print("fiskespot sodra finns")
        aut.moveTo(182, 323)
        aut.click()
        time.sleep(8)
    elif max_val <= 0.12 :
        print("sodra sidan finns ej, kollar de tvo andra")
        screenshot = ImageGrab.grab(bbox=(145, 305, 190, 365))#847, 214, 861, 228)
    screenshot.save("sample.png")
    screenshot.close()
    screenshot = np.array(Image.open("sample.png"))
    
    # Load the template image
    template = cv.imread("fisk.png")
    
    # Perform template matching
    result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    os.remove("sample.png")
    print("File 'sample.png' removed successfully.")
    if max_val >= 0.2:
        print("fiskespot sodra finns")
        aut.moveTo(336, 120)
        aut.click()
        time.sleep(8)
    elif max_val <= 0.2 :
        print("sodra sidan finns ej, kollar norra")
        screenshot = ImageGrab.grab(bbox=(245, 162  ,  289, 224))#847, 214, 861, 228)
    screenshot.save("sample.png")
    screenshot.close()
    screenshot = np.array(Image.open("sample.png"))
    
    # Load the template image
    template = cv.imread("fisk.png")
    
    # Perform template matching
    result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    os.remove("sample.png")
    print("File 'sample.png' removed successfully.")
    if max_val >= 0.2:
        print("fiskespot sodra finns")
        aut.moveTo(277, 203)
        aut.click()
        time.sleep(8)
    elif max_val <= 0.2 :
        time.sleep(4)
        pass





'''
kollavartvie

tra en bild på båda fiskeställena - om en av dem är över 0.9 så tryck på den
1a fiskestället - (vi står på norra ) södra stället 162, 311   195, 366 norra stället 260 162    289 224
2a fiskestället (vi ståpr på södra ) norra stället 320 93   352 135  södra stället 259, 168  289 212


droppa
fiska 
kolla inventory 
kollafiska 

1 kolla inventory - om ej full - kollafiskastatus - annars droppa - 

2 kollafiska - om ej fiska - fiska - annars låt gå(pass)

kolla vart vi är? 

'''
while True:

    kollainventory()
    time.sleep(1)
    kollafiskstatus()
    time.sleep(1)
    kollavartvie()
