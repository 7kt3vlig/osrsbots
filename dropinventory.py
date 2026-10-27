import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random





def drop28items():
    aut.PAUSE=0.05
    aut.moveTo(1733, 257) 
    aut.click()
    time.sleep(0.5)
    aut.moveTo(1733, 288)  
    aut.keyDown('shift')
    aut.click()
    for i in range(5):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift')  
             
    

    
    aut.moveTo(1776, 257)  
    aut.keyDown('shift')
    aut.click()
    for i in range(6):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift') 

    
    aut.moveTo(1818, 257)  
    aut.keyDown('shift')
    aut.click()
    for i in range(6):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift')  

    
    aut.moveTo(1860, 257)  
    aut.keyDown('shift')
    aut.click()
    for i in range(6):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift') 

    time.sleep(0.5)
    aut.moveTo(1415, 300) 
    aut.click()
    time.sleep(0.5)

#demon logs 
# for i in range (15):
#     drop28items()
#     # time.sleep(1200)
#     time.sleep(random.uniform(1000, 1200))

#fiska prif 
for i in range (400):
    drop28items()
    # time.sleep(1200)
    time.sleep(random.uniform(110, 120))