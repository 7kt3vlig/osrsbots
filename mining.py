import pyautogui as aut
import cv2 as cv 
import time 



def mining(): 

    for i in range(17):
        aut.moveTo(260, 190)
        time.sleep(1)
        aut.click()

        aut.moveTo(254, 197)
        time.sleep(1)
        aut.click()

    aut.moveTo(233, 255)
    aut.click()
    time.sleep(4)
    aut.moveTo(450, 341)
    aut.click()
    aut.press("esc")

    aut.moveTo(286, 156)
    aut.click()
    time.sleep(2.5)

def alkharidmining():
    aut.moveTo(240, 160)
    aut.click()
    time.sleep(1.8)

    aut.keyDown("shift")
    aut.moveTo(582, 257)
    
    aut.click()
    aut.moveTo(625, 257)
    
    aut.click()
    aut.moveTo(667, 257)
    
    aut.click()
    aut.keyUp("shift")



    aut.moveTo(257, 294)
    aut.click()
    time.sleep(1.8)

    aut.keyDown("shift")
    aut.moveTo(582, 257)
    
    aut.click()
    aut.moveTo(625, 257)
    
    aut.click()
    aut.moveTo(667, 257)
    
    aut.click()
    aut.keyUp("shift")



    aut.moveTo(188, 214)
    aut.click()
    time.sleep(1.8)


    aut.keyDown("shift")
    aut.moveTo(582, 257)
    
    aut.click()
    aut.moveTo(625, 257)
    
    aut.click()
    aut.moveTo(667, 257)
    
    aut.click()
    aut.keyUp("shift")

    
while True:
    alkharidmining()



#iron ore 5.4 sekunder respawn 
#1.2 sek 

    

