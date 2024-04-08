import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

def screen1fletch():

    aut.moveTo(367, 204)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(122, 82)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(449, 335) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(91, 118) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(140, 118) #ta logs  
    aut.click()
    time.sleep(0.2)
    aut.press("esc")


    aut.moveTo(583, 260) #knife inventory 
    time.sleep(0.2)
    aut.click()

    aut.moveTo(624, 260) #logs  
    time.sleep(0.2)
    aut.click()
    time.sleep(1)
    aut.press("space")

    #time.sleep(49)




def screen2fletch():

    aut.moveTo(1139, 200)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(895, 80)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(1221, 339) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(866, 120) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(914, 120) #ta logs  
    aut.click()
    time.sleep(0.2)
    aut.press("esc")


    aut.moveTo(1355, 252) #knife inventory 
    time.sleep(0.2)
    aut.click()

    aut.moveTo(1397, 252) #logs  
    time.sleep(0.2)
    aut.click()
    time.sleep(1)
    aut.press("space")

    


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

    screen1fletch()

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

    



def screen2345678alch():
    for i in range (12):

        aut.moveTo(1490, 336) #3
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        aut.moveTo(716, 839) #3
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        aut.moveTo(1491, 840) #4
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()
        
        
        aut.moveTo(2638, 336) #5
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        

        aut.moveTo(2638, 840) #6
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        aut.moveTo(3410, 840) #7
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        aut.moveTo(3410, 336 ) #8
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()


def screen34():
    for i in range (14):
        aut.moveTo(716, 839) #3
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        aut.moveTo(1491, 840) #4
        aut.click()
        time.sleep(0.2)
        aut.click()
        aut.click()

        time.sleep(1.8)



        


def screen5alch():
    aut.moveTo(2638, 336) #5
    aut.click()
    time.sleep(0.2)
    aut.click()
    aut.click()

    time.sleep(0.7)



def screen1craft():

    aut.moveTo(664, 118) #ta ammo mold 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)
    aut.moveTo(713, 118) #ta steel bars  
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)
    aut.press("esc")

    aut.moveTo(981, 139) #furnace
    time.sleep(0.2)
    aut.click()
    time.sleep(5)
    aut.moveTo(321, 311) #bracelet 
    time.sleep(0.2)
    aut.click()
    aut.press("space")
    time.sleep(160)

    aut.moveTo(645, 284)
    aut.click()
    time.sleep(7)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(1)

def screen678keepalive():
    aut.moveTo(3261, 437)
    aut.click()
    aut.click()

    aut.moveTo(3277, 839)
    aut.click()
    aut.click()

    aut.moveTo(2502, 909)
    aut.click()
    aut.click()

while True:
    screen1fletch()
    time.sleep(22)
    #screen2fletch()
    #screen34()
    #screen2345678alch()
    
    
    
        



    