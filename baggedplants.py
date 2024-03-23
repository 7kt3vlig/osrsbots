import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
 
def taenergy():
    aut.moveTo(936, 89) #energy tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(664, 118) #ta pot 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(1154, 254) #drick 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.8)

    hittaenbanker()

    aut.moveTo(1197, 254) #2nd spot inventory 
    aut.click()
    time.sleep(0.4)
    aut.moveTo(1197, 325)
    aut.click()

uppe = (580, 80)
nere = (1078, 327)

def hittafarmern():
    aut.moveTo(836, 192)
    aut.scroll(3000)
    
    

    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(uppe[0],uppe[1], nere[0], nere[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))

            # List of template images
            template_files = ["farmern.png", "farmern5.png", "farmern2.png", "farmern1.png"]

            for template_file in template_files:
                # Load the template image
                template = cv.imread(template_file)
            # Load the template image
            
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print(f"Template: {template_file}, Max Value: {max_val}, Location: ({max_loc[0] + uppe[0]}, {max_loc[1] + uppe[1]})")
            if max_val >= 0.8:
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + uppe[0]
                y = max_loc[1] + uppe[1]
                
                aut.moveTo(x + 5 , y + 10)
                aut.click(button="right")
                time.sleep(0.5)
                aut.moveTo(x + 5 , y + 32)
                aut.click()
                aut.moveTo(999, 108)
                aut.click(button="right")
                aut.moveTo(999, 196)
                aut.click()
                aut.press("esc")
                aut.moveTo(836, 192)
                aut.scroll(-3000)
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)


Top_left = (1194, 126)
Bottom_right = (1250, 150)

def hittabanken():
    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(Top_left[0],Top_left[1], Bottom_right[0], Bottom_right[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))
            
            # Load the template image
            template = cv.imread("bankikon2.png")
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("max val =", max_val)
            if max_val >= 0.7:
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + Top_left[0]
                y = max_loc[1] + Top_left[1]
                
                aut.moveTo(x + 5 , y + 5)
                aut.click()
                time.sleep(15)
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)

top_left = (1200, 54)
bottom_right = (1258, 100)

def dit():
    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(top_left[0],top_left[1], bottom_right[0], bottom_right[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))
            
            # Load the template image
            template = cv.imread("farmerikon.png")
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("max val =", max_val)
            if max_val >= 0.7:
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + top_left[0]
                y = max_loc[1] + top_left[1]
                
                aut.moveTo(x + 5 , y + 5)
                aut.click()
                time.sleep(18)
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)



roi_top_left = (706, 190)
roi_bottom_right = (939, 260)

def hittaenbanker():
    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(roi_top_left[0],roi_top_left[1], roi_bottom_right[0], roi_bottom_right[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))
            
            # Load the template image
            template = cv.imread("bankbooth.png")
            
            # Perform template matching
            result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print("max val =", max_val)
            if max_val >= 0.5:
                # Convert template coordinates to screen coordinates
                x = max_loc[0] + roi_top_left[0]
                y = max_loc[1] + roi_top_left[1]
                
                aut.moveTo(x + 50 , y + 2)
                aut.click()
                time.sleep(5)
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)


def banka():
    aut.moveTo(1197, 254) #2nd spot inventory 
    aut.click(button="right")
    time.sleep(0.4)
    aut.moveTo(1197, 325)
    aut.click()
    

def bytworld():
    aut.moveTo(1220, 504)
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(1306, 448)
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(1213, 446)
    aut.click(clicks=2)
    time.sleep(10)

    aut.moveTo(1221, 208)
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)
'''
while True:

    dit()
    hittafarmern()
    hittabanken()
    hittaenbanker()
    banka()
    taenergy()
    bytworld()
'''


hittafarmern()
