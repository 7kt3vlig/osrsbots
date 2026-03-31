import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random
    

def taenergy():
    aut.sleep(1.2) 
    aut.press("space")
    aut.sleep(0.7)  
    aut.press("2")
    aut.sleep(0.7)  
    aut.press("space")
    aut.sleep(0.7)  
    aut.press("space")
    aut.sleep(0.7)  
    aut.press("1")
    aut.sleep(0.7)  
    aut.press("space")
     
def hållmusenöverbetty():
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
        aut.moveTo(mus_x, mus_y, duration=0.2)
    else:
        print("Hittade inget i den valda zonen.")
def högerclicka():
    aut.click(button="right")
    aut.sleep(0.4)
    aut.moveRel(0,40)
    aut.click()


def zentrees():
    aut.moveTo(956,250)
    time.sleep(0.5)
    aut.click()
    time.sleep(3)
    aut.press("1")
    time.sleep(1.4)
    aut.moveTo(1010,336)
    aut.click()
    time.sleep(1)
    aut.press("1")
    time.sleep(1)
    


    aut.moveTo(1010,336)
    aut.click()
    time.sleep(1)
    aut.press("1")
    time.sleep(1.4)
    aut.moveTo(1010,336)
    aut.click()
    time.sleep(1)
    aut.press("1")
    time.sleep(1)

    aut.moveTo(1010,336)
    aut.click()
    time.sleep(1)
    aut.press("1")
    time.sleep(1.4)
    aut.moveTo(1010,336)
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("1")
    time.sleep(1)


    aut.moveTo(1415,404) #tp till guild 
    aut.click()
    time.sleep(1)


# def bank():

#     aut.moveTo(1225,233)#gå till banken
#     aut.click()
#     time.sleep(4)



#     aut.moveTo(1455,405)
#     aut.click()
#     time.sleep(0.7)
#     aut.moveTo(1220,310)
#     aut.click()
#     time.sleep(0.7)
#     aut.moveTo(1170,310)
#     aut.click()
#     time.sleep(0.7)
#     aut.moveTo(1170,350)
#     aut.click()
#     time.sleep(0.7)
#     aut.moveTo(1220,350)
#     aut.click()
#     time.sleep(1)
#     aut.press("esc")
#     aut.moveTo(1370,400)
#     aut.click()

def thieving():
    aut.moveTo(1225,300)
    aut.click()
    time.sleep(9.6)
    aut.moveTo(850,340)
    aut.click()
    time.sleep(4.8)
    
def construction():
    for i in range(4):
        aut.moveTo(1050,450)
        aut.click()
        time.sleep(0.8)
        aut.press("1")
        time.sleep(1.2)
        aut.moveTo(1050,450)
        aut.click()
        time.sleep(0.8)
        aut.press("1")
        time.sleep(0.8)

    # aut.moveTo(910,375)
    # aut.click()
    # time.sleep(0.8)
    # aut.press("1")
    # time.sleep(9)

def paybutler10k():
    aut.moveTo(910,375)
    aut.click()
    time.sleep(0.8)
    aut.press("space")
    time.sleep(1)
    aut.press("1")
    time.sleep(1)
    aut.press("space")



def bank():
    aut.moveTo(1458,419) #banka kannan
    aut.click()
    time.sleep(1)
    aut.moveTo(1225,233)
    aut.click()
    time.sleep(1)
    aut.moveTo(1220,310)
    aut.click()
    time.sleep(1)
    aut.moveTo(1170,310)
    aut.click()
    time.sleep(1)
    aut.moveTo(1170,350)
    aut.click()
    time.sleep(1)
    aut.moveTo(1220,350)
    aut.click()
    time.sleep(1)
    aut.press("esc")
    aut.moveTo(1370,420)
    aut.click()
    

# while True:
        
#     zentrees()
#     time.sleep(random.uniform(1, 20))
#     aut.moveTo(1225, 233)
#     aut.click()
#     time.sleep(5)
#     bank()
#     time.sleep(5)




while True:
    hållmusenöverbetty()
    aut.sleep(0.5)
    högerclicka()
    taenergy()



