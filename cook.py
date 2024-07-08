import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

def screen1craft():

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

    time.sleep(49)

def herb():
    aut.moveTo(367, 710)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(163, 597)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(448, 844) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(143, 633) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.press("esc")


def click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            aut.moveTo(x, y)
            aut.click()

# Define the starting point and offsets
start_x = 585
start_y = 762
x_offset = 42
y_offset = 37
num_rows = 7
num_cols = 4


def herbclean():
        
    while True:
        herb()
        click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
            

def koka():
    aut.moveTo(158, 207)  #banker
    aut.click()
    time.sleep(0.7)

    aut.moveTo(122, 90)  #shark tabben
    aut.click()
    time.sleep(0.2)

    aut.moveTo(450, 340) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(91, 130) #ta sharks 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(263, 141) #elden 
    time.sleep(0.4)
    aut.click()
    time.sleep(1)
    aut.press("space")

    time.sleep(65)


def screen2herb():

    aut.moveTo(367, 710)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(163, 597)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(448, 844) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(143, 633) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(90, 633) #ta logs  
    aut.click()
    time.sleep(0.2)
    aut.press("esc")


    aut.moveTo(625, 870) #knife inventory 
    time.sleep(0.2)
    aut.click()

    aut.moveTo(666, 874) #logs  
    time.sleep(0.2)
    aut.click()
    time.sleep(1)
    aut.press("space")

    # time.sleep(9)
 


def supercombat():
    aut.moveTo(367, 710)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(163, 597)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(448, 844) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(143, 633) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(189, 633) #ta atk pot
    aut.click()
    time.sleep(0.2)

    aut.moveTo(237, 633) #ta str pot   
    aut.click()
    time.sleep(0.2)

    aut.moveTo(285, 633) #ta def pot   
    aut.click()
    time.sleep(0.2)
    aut.press("esc")


    aut.moveTo(585, 764) #torstol inventory 
    time.sleep(0.2)
    aut.click()

    aut.moveTo(710, 805) #pot  
    time.sleep(0.2)
    aut.click()
    time.sleep(1)
    aut.press("space")



while True:
    koka()

    # screen1craft()

    # time.sleep(4)  
    # supercombat()
    # time.sleep(8)
    # supercombat()
    # time.sleep(8)
    # supercombat()
    # time.sleep(8)
    # supercombat()
 
    # for i in range(8):
    #     herb()
    #     click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
    

     
    # time.sleep(5)  
    # screen2herb() 
    # time.sleep(9) 
    # screen2herb()
    # time.sleep(9)
    # screen2herb() 
    # time.sleep(9)
    # screen2herb()

 