import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

def smith():
        
    aut.moveTo(93, 127) #ta ammo mold 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)
    aut.moveTo(144, 129) #ta steel bars  
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)
    aut.press("esc")

    aut.moveTo(407, 146) #furnace
    time.sleep(0.2)
    aut.click()
    time.sleep(5)
    aut.press("space")

def mina():
        

    for i in range (25):

        aut.moveTo(1020, 163)
        time.sleep(0.2)
        aut.click()
        time.sleep(1)

        aut.keyDown("shift")
        time.sleep(0.2)
        aut.moveTo(1361, 258)
        aut.click()
        aut.moveTo(1403, 258)
        aut.click()
        aut.keyUp("shift")

        aut.moveTo(952, 213)
        time.sleep(0.2)
        aut.click()
        time.sleep(1)

        aut.keyDown("shift")
        time.sleep(0.2)
        aut.moveTo(1361, 258)
        aut.click()
        aut.moveTo(1403, 258)
        aut.click()
        aut.keyUp("shift")
        


        aut.moveTo(1032, 291)
        time.sleep(0.2)
        aut.click()
        time.sleep(1)

        aut.keyDown("shift")
        time.sleep(0.2)
        aut.moveTo(1361, 258)
        aut.click()
        aut.moveTo(1403, 258)
        aut.click()
        aut.keyUp("shift")

def banka():
    aut.moveTo(79, 290)
    aut.click()
    time.sleep(7)

    aut.moveTo(452, 341) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(1)


while True:
    smith()
    mina()
    banka()



















aut.moveTo(645, 284)
aut.click()
time.sleep(7)

aut.moveTo(1021, 335) #banka allt 
time.sleep(0.5)
aut.click()
time.sleep(1)
