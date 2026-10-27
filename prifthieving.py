import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random
    




 
def prif():
    aut.FAILSAFE = True

    # 1. BESTÄM OMRÅDET (x, y, bredd, höjd)
    # Här letar vi i en ruta som startar vid 0,0 och är 960x540 pixlar
    region_x, region_y, region_w, region_h =1150, 19, 1671, 361

    # 2. TA BILDEN ENBART DÄR
    screenshot = aut.screenshot(region=(region_x, region_y, region_w, region_h))
    frame = np.array(screenshot)

    # (Färgkonvertering och maskning - samma som innan)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])
    mask = cv.inRange(hsv, lower_pink, upper_pink)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(largest)

        # 3. JUSTERA MUSPOSITIONEN
        # Vi lägger till 'region_x' och 'region_y' så musen hittar rätt på hela skärmen
        mus_x = x + w // 2 + region_x
        mus_y = y + h // 2 + region_y

        print(f"Hittade Betty i zonen vid: {mus_x}, {mus_y}")
        aut.moveTo(mus_x, mus_y, duration=0.1)
        aut.click()
    else:
        print("Hittade inget i den valda zonen.")




count = 0

while True:

    prif()
    time.sleep(60)
    aut.click(1816, 331)
    aut.click(1816, 331)
    time.sleep(2)
    # count += 1
    # if count == 20: # 110 x 0.5 sek = 55 sekunder
    #     # aut.press('4')
    #     aut.click(1812, 309) # Dina koordinater
    #     # time.sleep(0.5)
    #     # aut.press('2')
    #     count = 0 # Nollställ 55-sekunders-räknaren
    # time.sleep(0.5)
