import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 



for i in range (1000):
        aut.moveTo(1320, 155) # runewild 
        time.sleep(0.2)
        aut.click()
        time.sleep(1)
        aut.moveTo(1670, 260) # runewild 
        time.sleep(0.2)
        aut.keyDown("shift")
        aut.click()
        aut.keyUp("shift")
        time.sleep(4)

