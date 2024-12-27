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
    time.sleep(0.6)

    aut.moveTo(625, 372)  
    aut.click()
    time.sleep(0.6)
    aut.moveTo(669, 368)  
    aut.click()

    time.sleep(0.9)
    aut.press("space")
    time.sleep(17.5)

def stamina():
    aut.moveTo(369, 204)  #banker
    aut.click()
    time.sleep(0.6)

    aut.moveTo(450, 340)  #banka allt
    aut.click()
    time.sleep(0.6)
    

    aut.moveTo(93, 165)  #seeds
    aut.click()
    time.sleep(0.6)

    aut.moveTo(140, 165)  #energy
    aut.click()
    time.sleep(0.6)

    aut.press("esc")
    time.sleep(0.6)

    aut.moveTo(585, 255)  
    aut.click()
    time.sleep(0.6)

    aut.moveTo(625, 255)  
    aut.click()

    time.sleep(0.9)
    aut.press("space")
    time.sleep(32)

def supercombat():

    aut.moveTo(369, 204)  #banker
    aut.click()
    time.sleep(0.6)

    aut.moveTo(450, 340)  #banka allt
    aut.click()
    time.sleep(0.6)
    

    aut.moveTo(93, 130)  #torstol
    aut.click()
    time.sleep(0.6)

    aut.moveTo(142, 130)  #def
    aut.click()
    time.sleep(0.6)

    aut.moveTo(190, 130)  #att
    aut.click()
    time.sleep(0.6)

    aut.moveTo(240, 130)  #str
    aut.click()
    time.sleep(0.6)

    aut.press("esc")
    time.sleep(0.6)

    aut.moveTo(585, 260)  
    aut.click()
    time.sleep(0.6)

    aut.moveTo(585, 336)  
    aut.click()

    time.sleep(0.9)
    aut.press("space")
    time.sleep(9)



while True:
    supercombat()
    # herb()
    # stamina()

