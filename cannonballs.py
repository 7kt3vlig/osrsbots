import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 


def smith():

    aut.moveTo(664, 118) #ta ammo mold 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)
    aut.moveTo(713, 118) #ta steel bars  
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)
    aut.press("esc")

    aut.moveTo(981, 139) #furnace
    time.sleep(0.2)
    aut.click()
    time.sleep(5)
    aut.press("space")
    time.sleep(160)

    aut.moveTo(645, 284)
    aut.click()
    time.sleep(7)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(1)



while True:
    smith()



aut.keyDown("up")
time.sleep(3)
aut.keyUp("up")

aut.press("enter")
time.sleep(10)