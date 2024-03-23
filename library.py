import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 


def centrera():

    aut.moveTo(1138, 42) 
    time.sleep(1)
    aut.click()
    time.sleep(1)


def uppåt():
    aut.keyDown("up")
    time.sleep(3)
    aut.keyUp("up")
    

#minimap koordinater övre vänster 1160, 34 , 1160 154 nedre vänster 
    #övre höger 1288, 34 nedre höger 1288,154