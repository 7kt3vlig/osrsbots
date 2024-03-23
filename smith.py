import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

while True:

    aut.moveTo(664, 120) #bronze bar 
    aut.click()
    time.sleep(0.4)

    aut.moveTo(712, 120) #hammer 
    time.sleep(0.5)
    aut.click()
    time.sleep(1)

    aut.press("esc")

    aut.moveTo(891, 358) #anvil 
    time.sleep(0.5)
    aut.click()
    time.sleep(8)


    aut.moveTo(778, 88) # chainbodys 
    time.sleep(0.5)
    aut.click()
    time.sleep(40)


    aut.moveTo(814, 95) # banken 
    time.sleep(0.5)
    aut.click()
    time.sleep(10)

    aut.moveTo(1022, 336) # banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(7)



    