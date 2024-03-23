import pyautogui as aut
import numpy
import cv2 as cv 
import time 
import win32 

aut.moveTo(1027, 314)
aut.click()
time.sleep(0.4)

aut.write('bandy-peter', interval=0.25)

aut.hotkey('altright','2')

aut.write('live.se', interval=0.25)
aut.press("tab")

aut.write('Gandalfdentredje333', interval=0.25)

aut.press("enter")

aut.moveTo(960, 360)
aut.click()
time.sleep(0.4)