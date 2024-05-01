import pyautogui as aut
import time 


def herb():
    aut.moveTo(369, 204)  #banker
    aut.click()
    time.sleep(0.6)

    aut.moveTo(450, 340)  
    aut.click()
    

    aut.moveTo(142, 129)  
    aut.click()
    time.sleep(0.6)

    aut.moveTo(91, 133)  
    aut.click()
    time.sleep(0.6)
    aut.press("esc")

    aut.moveTo(625, 372)  
    aut.click()
    time.sleep(0.2)
    aut.moveTo(669, 368)  
    aut.click()

    time.sleep(0.6)
    aut.press("space")
    time.sleep(9)

while True:
        
    herb()

