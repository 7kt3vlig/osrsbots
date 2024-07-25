import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os


# aut.moveTo(544, 240) #start, från slutet
# aut.click()
# time.sleep(5)

def plantrundaosmtartrekannor():
        
    aut.moveTo(1245, 490) #BÖRJA HÖGST UPP 
    aut.click()
    aut.moveTo(514, 386) 
    aut.click()
    time.sleep(2)
    aut.click()
    time.sleep(3)


    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(628, 388) 
    aut.click()
    time.sleep(3)
    aut.click()
    time.sleep(3)

    #"andra raden "

    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(489, 436) 
    aut.click()
    time.sleep(3)
    aut.moveTo(489, 391) 
    aut.click()
    time.sleep(3)


    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(628, 391) 
    aut.click()
    time.sleep(3)
    aut.click()
    time.sleep(3)


    #tredje raden

    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(489, 436) 
    aut.click()
    time.sleep(3)
    aut.moveTo(489, 391) 
    aut.click()
    time.sleep(3)


    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(628, 391) 
    aut.click()
    time.sleep(3)
    aut.click()
    time.sleep(3)


    #fjärde raden 

    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(489, 436) 
    aut.click()
    time.sleep(3)
    aut.moveTo(489, 391) 
    aut.click()
    time.sleep(3)


    aut.moveTo(1245, 490) 
    aut.click()
    aut.moveTo(628, 391) 
    aut.click()
    time.sleep(3)
    aut.click()
    time.sleep(3)

    aut.moveTo(544, 240) #start, från slutet
    aut.click()
    time.sleep(11)

    #vattenrunda 2

    aut.moveTo(517, 389) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(5)

    #gå till start 

    aut.moveTo(544, 240) 
    aut.click()
    time.sleep(5)

    #vattenrunda 3

    aut.moveTo(517, 389) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(4) 

    #gå till start 
    aut.moveTo(544, 240) 
    aut.click()
    time.sleep(7)

    #harvest 

    aut.moveTo(517, 389) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(7)

    aut.moveTo(492, 451) 
    aut.click()
    time.sleep(7)

    aut.moveTo(626, 386) 
    aut.click()
    time.sleep(4) 

    



def fyllvattenkannorna():
    time.sleep(1)
    aut.moveTo(1522, 923) 
    aut.click()
    time.sleep(0.4)
    aut.moveTo(431, 475) 
    aut.click()
    time.sleep(38)
    aut.moveTo(605, 187)
    aut.click()
    time.sleep(10)


while True:
        
    
    plantrundaosmtartrekannor()
    #gå till start 
    aut.moveTo(544, 240) 
    aut.click()
    time.sleep(5)
    plantrundaosmtartrekannor()
    aut.moveTo(544, 240) 
    aut.click()
    time.sleep(5)
    plantrundaosmtartrekannor()
    aut.moveTo(544, 240) 
    aut.click()
    time.sleep(5)
    plantrundaosmtartrekannor()
    aut.moveTo(544, 240) 
    aut.click()
    time.sleep(5)
    plantrundaosmtartrekannor()

    fyllvattenkannorna()