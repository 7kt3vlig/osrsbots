import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 



def loggain():

    aut.moveTo(958, 323)
    aut.click()
    time.sleep(0.4)
    
    aut.moveTo(1027, 314)
    aut.click()
    time.sleep(0.4)

    aut.write('bandy-peter', interval=0.25)

    aut.hotkey('altright','2')

    aut.write('live.se', interval=0.25)
    aut.press("tab")

    aut.write('Gandalfdentredje333', interval=0.25)

    aut.press("enter")
    time.sleep(10)

    aut.moveTo(960, 360)
    aut.click()
    time.sleep(3)


    aut.keyDown("up")
    time.sleep(3)
    aut.keyUp("up")

def koka():
    aut.moveTo(730, 207)  #banker
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

    aut.moveTo(1155, 249) #sharks inventory 
    time.sleep(0.4)
    aut.click()

    aut.moveTo(837, 102) #elden 
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("space")

    time.sleep(65)



def kokasextimmar():
    rundor = 0 
    while rundor < 299:
        koka()
    rundor+1 
    time.sleep(300)
    

def sleep():
    time.sleep(21600)





while True:

    kokasextimmar()
    sleep()
    loggain()