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
    time.sleep(5)


    aut.moveTo(366, 97) # chainbodys 
    time.sleep(0.2)
    aut.click()
    # time.sleep(81)

    for i in range (18):
        aut.moveTo(1320, 155) # runewild 
        time.sleep(0.2)
        aut.click()
        time.sleep(1)
        aut.moveTo(1670, 260) # runewild 
        time.sleep(0.2)
        aut.keyDown("shift")
        aut.click()
        aut.keyUp("shift")
        time.sleep(2.6)


    aut.moveTo(248, 107) # banken 
    time.sleep(0.2)
    aut.click()
    time.sleep(5)

    aut.moveTo(450, 340) # banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)



    