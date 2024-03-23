import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 


def fletcha():


    aut.moveTo(1155, 260) #knife inventory 
    time.sleep(0.4)
    aut.click()

    aut.moveTo(1200, 260) #logs  
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("space")




def alcha():

    for i in range(4):
        aut.moveTo(560, 732)
        time.sleep(0.5)
        aut.click()
        time.sleep(0.2)
        aut.click()
        time.sleep(2)


while True:
    fletcha()
    alcha()


