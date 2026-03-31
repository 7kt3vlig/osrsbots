import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random
import time 




def slow():

    aut.moveTo(607, 234)
    aut.click()
    time.sleep(14)

    aut.moveTo(759, 199)
    aut.click()
    time.sleep(12)

    aut.moveTo(736, 156)
    aut.click()
    time.sleep(10)

    aut.moveTo(765, 204)
    aut.click()
    time.sleep(16)

    aut.moveTo(883, 266)
    aut.click()
    time.sleep(7)

    aut.moveTo(1040, 189)
    aut.click()
    time.sleep(15)

    aut.moveTo(1021, 159)
    aut.click()
    time.sleep(13)

    aut.moveTo(842, 124)
    aut.click()
    time.sleep(9)

    aut.moveTo(842, 138)
    aut.click()
    time.sleep(8)



def fast():
    aut.moveTo(607, 234)
    aut.click()
    time.sleep(9)

    aut.moveTo(759, 199)
    aut.click()
    time.sleep(9)

    aut.moveTo(736, 156)
    aut.click()
    time.sleep(7)

    aut.moveTo(765, 204)
    aut.click()
    time.sleep(12)

    aut.moveTo(883, 266)
    aut.click()
    time.sleep(5)

    aut.moveTo(1040, 189)
    aut.click()
    time.sleep(11)

    aut.moveTo(1021, 159)
    aut.click()
    time.sleep(10)

    aut.moveTo(842, 124)
    aut.click()
    time.sleep(4)

    aut.moveTo(842, 138)
    aut.click()
    time.sleep(5)


def togglerun():
    aut.moveTo(1144, 146)
    time.sleep(1)
    aut.click()
    
def falador():
    aut.moveTo(918, 112) #1
    aut.click()
    time.sleep(5)

    aut.moveTo(890, 180)#2
    aut.click()
    time.sleep(8)

    aut.moveTo(870, 133)#3
    aut.click()
    time.sleep(10)

    aut.moveTo(814, 171)#4
    aut.click()
    time.sleep(3)

    aut.moveTo(785, 194)#5
    aut.click()
    time.sleep(4)

    aut.moveTo(746, 190)#6
    aut.click()
    time.sleep(10)

    aut.moveTo(810, 207)#7
    aut.click()
    time.sleep(5)

    aut.moveTo(811, 199)#8
    aut.click()
    time.sleep(3)

    aut.moveTo(809, 241)#9
    aut.click()
    time.sleep(3.5)

    aut.moveTo(824, 226)#10
    aut.click()
    time.sleep(3)

    aut.moveTo(851, 300)#11
    aut.click()
    time.sleep(5)

    aut.moveTo(900, 195)#12
    aut.click()
    time.sleep(3.5)

    aut.moveTo(905, 203)#13
    aut.click()
    time.sleep(5)







########################################################################
def prifdinnas(): # kamera 129 som falador 
    # 1
    aut.moveTo(1030, 195)
    aut.click()
    time.sleep(random.uniform(8, 11))

    # 2
    aut.moveTo(870, 250)
    aut.click()
    time.sleep(random.uniform(14, 20))

    # 3
    aut.moveTo(850, 170)
    aut.click()
    time.sleep(random.uniform(6, 11))

    # 4
    aut.moveTo(840, 155)
    aut.click()
    time.sleep(random.uniform(5, 11))

    # 5
    aut.moveTo(840, 185)
    aut.click()
    time.sleep(random.uniform(5, 11))

    # 6
    aut.moveTo(850, 135)
    aut.click()
    time.sleep(random.uniform(5, 11))

    # 7
    aut.moveTo(765, 240)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 8
    aut.moveTo(790, 200)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 9
    aut.moveTo(825, 175)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 10
    aut.moveTo(805, 165)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 11
    aut.moveTo(880, 175)
    aut.click()
    time.sleep(random.uniform(8, 11))

    # 12
    aut.moveTo(815, 130)
    aut.click()
    time.sleep(random.uniform(9, 16))

    # 13 (Väntetid efter sista klicket innan loopen börjar om)
    time.sleep(random.uniform(1, 10))


def prifdinnas2(): #kamera 129 som falador 
    aut.moveTo(1030, 195) #1
    aut.click()
    time.sleep(8)

    aut.moveTo(870, 250)#2
    aut.click()
    time.sleep(14)

    aut.moveTo(850, 170)#3
    aut.click()
    time.sleep(6)

    aut.moveTo(840, 155)#4
    aut.click()
    time.sleep(5)

    aut.moveTo(840, 185)#5
    aut.click()
    time.sleep(5)

    aut.moveTo(850, 135)#6
    aut.click()
    time.sleep(5)

    aut.moveTo(765, 240)#7
    aut.click()
    time.sleep(9)

    aut.moveTo(790,200)#8
    aut.click()
    time.sleep(9)

    aut.moveTo(825, 175)#9
    aut.click()
    time.sleep(9)

    aut.moveTo(805, 165)#10
    aut.click()
    time.sleep(9)

    aut.moveTo(880, 175)#11
    aut.click()
    time.sleep(8)

    aut.moveTo(815, 130)#12
    aut.click()
    time.sleep(9)



# --- Inställningar ---
# Definiera det område du vill bevaka: (left, top, width, height)
# Tips: Använd pyautogui.position() för att hitta koordinaterna.
MONITOR_REGION = (583, 36, 1077, 352) 

# Definiera "Rosa" i HSV-färgrymd (Hue, Saturation, Value)
# Dessa värden täcker de flesta starkrosa nyanser.
PINK_LOWER = np.array([140, 50, 50])
PINK_UPPER = np.array([170, 255, 255])

def scan_and_interact():
    # 1. Ta screenshot EXAKT på dina koordinater
    screenshot = ImageGrab.grab(bbox=MONITOR_REGION)

    frame = np.array(screenshot)
    frame_bgr = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, PINK_LOWER, PINK_UPPER)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        M = cv.moments(largest_contour)
        if M["m00"] != 0:
            # 2. Räkna ut lokalt center i bilden
            local_x = int(M["m10"] / M["m00"])
            local_y = int(M["m01"] / M["m00"])
            
            # 3. Addera startpunkten (583, 36) för att få rätt skärmplats
            global_x = local_x + MONITOR_REGION[0]
            global_y = local_y + MONITOR_REGION[1]
            
            print(f"Hittade rosa! Klickar på: ({global_x}, {global_y})")
            aut.click(global_x, global_y + 10)
            return True
    
    return False

def smart_click(x, y):
    # Försök hitta rosa först
    found_pink = scan_and_interact()
    
    # Om ingen rosa hittades, klicka på de fasta koordinaterna
    if not found_pink:
        print(f"Inget rosa, klickar på backup: ({x}, {y})")
        aut.click(x, y)
        aut.click(x, y)

def prifdinnas3(): #kamera 129 som falador 

    smart_click(1030, 195)
    time.sleep(8)

    smart_click(870, 250)
    time.sleep(14)

    smart_click(850, 170)
    time.sleep(6)

    smart_click(840, 155)
    time.sleep(5)

    smart_click(840, 185)
    time.sleep(5)

    smart_click(850, 135)
    time.sleep(5)

    smart_click(765, 240)
    time.sleep(9)

    smart_click(790,200)
    time.sleep(9)

    smart_click(825, 175)
    time.sleep(9)

    smart_click(805, 165)
    time.sleep(9)

    smart_click(880, 175)
    time.sleep(8)

    smart_click(815, 130)
    time.sleep(9)


def ardy(): #kamera 129 som falador 
    aut.moveTo(1030, 195) #1
    aut.click()
    time.sleep(8)

    aut.moveTo(870, 250)#2
    aut.click()
    time.sleep(14)

    aut.moveTo(850, 170)#3
    aut.click()
    time.sleep(6)

    aut.moveTo(840, 155)#4
    aut.click()
    time.sleep(5)

    aut.moveTo(840, 185)#5
    aut.click()
    time.sleep(5)

    aut.moveTo(850, 135)#6
    aut.click()
    time.sleep(5)

    aut.moveTo(765, 240)#7
    aut.click()
    time.sleep(9)



def tabild():
    try:
        screenshot = ImageGrab.grab(bbox=(581, 26, 1093, 361))#847, 214, 861, 228)
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        
        # Load the template image
        template = cv.imread("pillar.png")
        
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
            aut.moveTo(836, 169)
            time.sleep(1)
            aut.click()
            time.sleep(3)
        elif max_val >= 0.8:
            aut.moveTo(836, 184)
            time.sleep(1)
            aut.click()
            time.sleep(3)
        else:
            pass

'''
while True:


    for i in range (2):
        slow()

    togglerun()
    for i in range (10):
        fast()

    togglerun()
'''
#kamera 102, 129 
#en runda tar 68-69 sekunder
# for i in range(360):
#     tabild()
#     falador()


while True:

    prifdinnas2()