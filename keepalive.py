import pyautogui as aut
import cv2 as cv 
import time 

while True:
        
    for i in range(50):
            
        aut.moveTo(282, 141)
        aut.click()
        time.sleep(0.6)
    
    aut.moveTo(606, 259)
    aut.click()
    aut.click()
    time.sleep(0.6)

    