
import pyautogui as aut
import time 

while True:

    aut.moveTo(501, 396) 
    
    aut.click()
    time.sleep(1.2)
    aut.keyDown("shift")
    aut.moveTo(841, 454)
    aut.click()
    aut.keyUp("shift")
    time.sleep(1.5)


