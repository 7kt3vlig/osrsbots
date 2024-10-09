import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 


def fast():

    aut.moveTo(600, 264)
    aut.click()
    time.sleep(10)

    aut.moveTo(837, 206)
    aut.click()
    time.sleep(4)

    aut.moveTo(823, 202)
    aut.click()
    time.sleep(6)

    aut.moveTo(824, 192)
    aut.click()
    time.sleep(5)

    aut.moveTo(1020, 357)
    aut.click()
    time.sleep(7)

    aut.moveTo(849, 161)
    aut.click()
    time.sleep(10)



while True: 
        
    fast()