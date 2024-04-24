import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 
from ardyknight3 import detect_coin_pouches, ardyknight 


while True:
    for i in range (30):
        ardyknight()
        
    aut.moveTo(582, 260)
    time.sleep(0.2)
    aut.click()
    aut.click()
    aut.click()

            # Increment the iteration counter
           
