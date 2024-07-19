import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

while True:

    aut.moveTo(138, 128) #hammer   
    aut.click()
    time.sleep(0.2)

    aut.moveTo(95, 126) #bar  
    time.sleep(0.2)
    aut.click()
    

    aut.press("esc")

    aut.moveTo(315, 361) #anvil 
    time.sleep(0.2)
    aut.click()
    time.sleep(4)


    aut.moveTo(205, 259) # chainbodys 
    time.sleep(0.2)
    aut.click()
    time.sleep(15)


    aut.moveTo(241, 98) # banken 
    time.sleep(0.2)
    aut.click()
    time.sleep(4)

    aut.moveTo(450, 340) # banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)



    