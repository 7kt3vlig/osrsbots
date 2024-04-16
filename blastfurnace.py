import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 

def runda():
    aut.moveTo(94, 127) #ta bars 
    aut.click()
    time.sleep(0.6)
    aut.press("esc")

    aut.moveTo(206, 90) #tryck på grejen för att göra bars 
    aut.click()
    time.sleep(6.6)

    aut.press("1")
    time.sleep(4.6)


    aut.moveTo(238, 256) #hämta bars 
    time.sleep(0.2)
    aut.click()
    time.sleep(3.6)
    aut.press("space")
    time.sleep(0.6)

    aut.moveTo(400, 322) #bank
    aut.click()
    time.sleep(4.2)


    aut.moveTo(450, 340)
    aut.click()
    time.sleep(0.2)


def drickenergy():
    aut.moveTo(283, 94) #energy tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(92, 133) #ta pot 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(582, 263) #drick 
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

    aut.moveTo(245, 88)
    aut.click()
    time.sleep(0.2)


while True:
        
    for i in range (5):
        runda()

    drickenergy()