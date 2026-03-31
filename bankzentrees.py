
import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 


def bank():

    aut.moveTo(1206,241)#gå till banken
    aut.click()
    time.sleep(4)



    aut.moveTo(1455,405)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1220,310)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1170,310)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1170,350)
    aut.click()
    time.sleep(0.7)
    aut.moveTo(1220,350)
    aut.click()
    time.sleep(1)
    aut.press("esc")
    aut.moveTo(1370,400)
    aut.click()

bank()