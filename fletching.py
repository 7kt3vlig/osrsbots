import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

def screen1():

    aut.moveTo(940, 204)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(695, 82)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(664, 118) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(712, 118) #ta logs  
    aut.click()
    time.sleep(0.2)
    aut.press("esc")


    aut.moveTo(1155, 260) #knife inventory 
    time.sleep(0.2)
    aut.click()

    aut.moveTo(1200, 260) #logs  
    time.sleep(0.2)
    aut.click()
    time.sleep(1)
    aut.press("space")



def screen2():

    aut.moveTo(2861, 191)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(2616, 80)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(2942, 335) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(2586, 120) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(2633, 120) #ta logs  
    aut.click()
    time.sleep(0.2)
    aut.press("esc")


    aut.moveTo(3075, 252) #knife inventory 
    time.sleep(0.2)
    aut.click()

    aut.moveTo(3116, 252) #logs  
    time.sleep(0.2)
    aut.click()
    time.sleep(1)
    aut.press("space")

    time.sleep(45)


def screen3mining ():
    aut.moveTo(2744, 164)  #
    time.sleep(0.2)
    aut.click()
    time.sleep(1) 

    aut.keyDown("shift")
    aut.moveTo(3076, 288)  #droppa 1 
    aut.click()
    time.sleep(0.2)
    aut.moveTo(3118, 288)
    aut.click()
    aut.keyUp("shift")


    aut.moveTo(2706, 198)  #
    time.sleep(0.2)
    aut.click()
    time.sleep(1)

    aut.keyDown("shift")
    aut.moveTo(3076, 288)  #droppa 1 
    aut.click()
    time.sleep(0.2)
    aut.moveTo(3118, 288)
    aut.click()
    aut.keyUp("shift")



    aut.moveTo(2753, 249)  #
    time.sleep(0.2)
    aut.click()
    time.sleep(1)

    aut.keyDown("shift")
    aut.moveTo(3076, 288)  #droppa 1 
    aut.click()
    time.sleep(0.2)
    aut.moveTo(3118, 288)
    aut.click()
    aut.keyUp("shift")


def screen4smithing():

    

    aut.moveTo(2586, 120) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(2633, 120) #ta logs  
    aut.click()
    time.sleep(0.2)

    aut.press("esc")

    aut.moveTo(2808, 357) #anvil 
    time.sleep(0.5)
    aut.click()
    time.sleep(8)


    aut.moveTo(2699, 252) # chainbodys 
    time.sleep(0.5)
    aut.click()

    screen1()

    time.sleep(20)


    aut.moveTo(2734, 94) # banken 
    time.sleep(0.5)
    aut.click()
    time.sleep(10)

    aut.moveTo(2941, 336) # banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(7)

def screen2prayer():

    for i in range (28):
        aut.moveTo(3207, 469) #  
        aut.click()

        aut.moveTo(2745, 191) #  
        aut.click()
        time.sleep(0.1)
        
def screen2alch():
    for i in range(22):
        aut.moveTo(3210, 334)
        aut.click()
        time.sleep(0.2)
        aut.click()
        time.sleep(2.5)

def screen1cook():

    aut.moveTo(730, 207)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.7)

    aut.moveTo(774, 80)  #shark tabben
    aut.click()
    time.sleep(0.2)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(664, 118) #ta sharks 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(837, 102) #elden 
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("space")

def screen2cook():

    aut.moveTo(2080, 223)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.7)

    aut.moveTo(2083, 87)  #shark tabben
    aut.click()
    time.sleep(0.2)

    aut.moveTo(2370, 341) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(2011, 123) #ta sharks 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(2184, 132) #elden 
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("space")

    time.sleep(59)



def screen345keepalive():
    aut.moveTo(3272, 215) #3
    time.sleep(0.4)
    aut.click()

    aut.moveTo(2502, 718) #4
    time.sleep(0.4)
    aut.click()

    aut.moveTo(3274, 715) #5
    time.sleep(0.4)
    aut.click()






while True:
    
    screen1cook()
    screen2cook()
    screen345keepalive()
    
        



    