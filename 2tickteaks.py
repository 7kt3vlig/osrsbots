import pyautogui as aut
import cv2 as cv 
import time 

def autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            aut.moveTo(x, y)
            aut.click()
            

# Define the starting point and offsets
start_x = 3160
start_y = 565
x_offset = 88
y_offset = 73
num_rows = 6
num_cols = 4

autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset)

# while True:
        
    # for i in range (40):
    #     aut.moveTo(2640, 560)
    #     aut.click()
    #     time.sleep(0.4)
    

    #     aut.moveTo(2498, 565)
    #     aut.click()
    #     time.sleep(0.4)

   


    
