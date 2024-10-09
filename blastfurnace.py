import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 

#kamera 127

def runda():
    aut.moveTo(430, 306) #ta bars 
    aut.click()
    time.sleep(0.6)
    aut.press("esc")

    aut.moveTo(588, 256) #byt gloves till gold
    aut.click()
    time.sleep(0.6)

    aut.moveTo(207, 92) #tryck på grejen för att göra bars 
    aut.click()
    time.sleep(12) 

    aut.moveTo(588, 256) #byt gloves till ice
    aut.click()
    time.sleep(0.6)

    aut.moveTo(223, 255) #stå bredvid bars
    aut.click()
    time.sleep(5)

    aut.moveTo(280, 191) #tryck på bars 
    aut.click()
    time.sleep(2)

    aut.press("space")
    time.sleep(1)


    aut.moveTo(414, 304) #bank
    aut.click()
    time.sleep(4.2)


    aut.moveTo(450, 340) #banka allt
    aut.click()
    time.sleep(0.2)


def drickenergy():
    

    aut.moveTo(188, 134) #ta pot 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(623, 263) #drick 
    time.sleep(0.6)
    aut.click()
    time.sleep(1)

    aut.moveTo(264, 211) #bankern 
    time.sleep(0.4)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(450, 340) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)


    

while True:
        
    for i in range (5):
        runda()

    drickenergy()