import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 
import multiprocessing
import math 
import threading 
import ctypes

def autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            aut.moveTo(x, y)
            aut.click()
            

# Define the starting point and offsets
start_x = 3165
start_y = 485
x_offset = 88
y_offset = 70
num_rows = 7
num_cols = 4

        
autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
