import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 


while True:

    aut.moveTo(940, 204)  #banker
    time.sleep(0.5)
    aut.click()
    time.sleep(1)

    aut.moveTo(695, 82)  #fletch tabben
    time.sleep(0.5)
    aut.click()
    time.sleep(0.4)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(664, 118) #ta knife 
    aut.click()
    time.sleep(0.4)

    aut.moveTo(712, 118) #ta logs  
    aut.click()
    time.sleep(0.4)
    aut.press("esc")


    aut.moveTo(1155, 260) #knife inventory 
    time.sleep(0.4)
    aut.click()

    aut.moveTo(1200, 260) #logs  
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("space")

    time.sleep(49)