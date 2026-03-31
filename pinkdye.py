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
        
    # Optional safety
    aut.FAILSAFE = True

    # Take screenshot
    screenshot = aut.screenshot()
    frame = np.array(screenshot)

    # Convert RGB (PIL) → BGR (OpenCV)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    # Convert to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Pink color range (adjust if needed)
    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])

    # Mask
    mask = cv.inRange(hsv, lower_pink, upper_pink)

    # Clean noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)

    # Find contours
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv.contourArea)

        x, y, w, h = cv.boundingRect(largest)

        center_x = x + w // 2
        center_y = y + h // 2

        print(f"Shape found at: {center_x}, {center_y}")

        # Move mouse
        aut.moveTo(center_x, center_y, duration=0.2)
    else:
        print("No pink shape found")

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


def bank():

    aut.moveTo(1206,241)#gå till banken
    aut.click()
    time.sleep(4)



    aut.moveTo(1455,405)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1220,310)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1170,310)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1170,350)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1220,350)
    aut.click()
    time.sleep(1)
    aut.press("esc")
    aut.moveTo(1370,400)
    aut.click()

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
    aut.moveTo(1455,405)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1220,310)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1170,310)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1170,350)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1220,350)
    aut.click()
    time.sleep(1)
    aut.press("esc")
    aut.moveTo(1370,400)
    aut.click()
    

while True:
        
    zentrees()
    time.sleep(random.uniform(1, 20))
    aut.moveTo(1210, 220)
    aut.click()
    time.sleep(5)
    bank()
    time.sleep(5)




# while True:
#     hållmusenöverbetty()
#     aut.sleep(0.5)
#     högerclicka()
#     taenergy()



