import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 
import multiprocessing
import math 
import threading 
import ctypes

# Define the screen coordinates for both clicks
COORD1 = (387, 340)
COORD2 = (387, 833)

# Function to simulate mouse click at specified coordinates
def click_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Left mouse button down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Left mouse button up

def screen1():
    click_mouse(*COORD1)

def screen2():
    click_mouse(*COORD2)

if __name__ == '__main__':
    # Create threads for each screen action
    t1 = threading.Thread(target=screen1)
    t2 = threading.Thread(target=screen2)
    
    # Start both threads
    t1.start()
    t2.start()
    
    # Wait for both threads to finish
    t1.join()
    t2.join()


