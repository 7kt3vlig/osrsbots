import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os

def ta():
    
    start_time = time.time()
    


    aut.moveTo(925, 194) #thieving platsen 
    time.sleep(0.6)
    aut.click()
    aut.moveTo(1155, 253) #inventory 
    aut.keyDown("shift")
    time.sleep(2)
    aut.click()
    aut.keyUp("shift")

    # Check elapsed time
    elapsed_time = time.time() - start_time

    # Stop execution after 6 hours
    if elapsed_time >= 6 * 3600:  # 6 hours * 3600 seconds per hour
        print("Time limit reached. Stopping execution.")
        exit()  # or sys.exit() if you need to exit from a function or module


def timer():
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"Duration: {elapsed_time:.2f} seconds", end="\r")  # \r to overwrite the previous line
        time.sleep(1)

def fruitstall():
    
    while True:
        timer()
        ta()


uppe = (580, 80)
nere = (1078, 327)

def hittapaladin():
    
    condition_met = False
    while not condition_met:

        try:
            screenshot = ImageGrab.grab(bbox=(uppe[0],uppe[1], nere[0], nere[1] ))#847, 214, 861, 228)
            screenshot.save("sample.png")
            screenshot.close()
            screenshot = np.array(Image.open("sample.png"))

            # List of template images
            template_files = ["paladin.png", "paladin2.png"]

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
                
                aut.moveTo(x + 2 , y + 3)
                aut.click(button="right")
                time.sleep(0.5)
                aut.moveTo(x + 5 , y + 32)
                aut.click()
                aut.moveTo(999, 108)
                aut.click(button="right")
                aut.moveTo(999, 196)
                aut.click()
                aut.press("esc")
                
                condition_met = True
        except Exception as e:
            print("Error:", e)
        finally:
            try:
                os.remove("sample.png")
                print("File 'sample.png' removed successfully.")
            except Exception as e:
                print("Error while removing file:", e)

hittapaladin()
