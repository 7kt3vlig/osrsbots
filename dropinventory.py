import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 






def drop28items():
    aut.PAUSE=0.05
    aut.moveTo(1505, 404) 
    aut.click()
    time.sleep(0.5)
    aut.moveTo(1552, 443)  
    aut.keyDown('shift')
    aut.click()
    for i in range(5):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift')  
             
    

    
    aut.moveTo(1592, 404)  
    aut.keyDown('shift')
    aut.click()
    for i in range(6):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift') 

    
    aut.moveTo(1635, 404)  
    aut.keyDown('shift')
    aut.click()
    for i in range(6):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift')  

    
    aut.moveTo(1677, 404)  
    aut.keyDown('shift')
    aut.click()
    for i in range(6):
        aut.moveRel(0, 35)
        aut.keyDown('shift')  
        aut.click() 
        aut.keyUp('shift') 



for i in range (1):
    drop28items()