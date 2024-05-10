import pyautogui as aut
import time 

def herb():
    aut.moveTo(369, 204)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(1)

    aut.moveTo(450, 340)  
    aut.click()

    aut.moveTo(142, 129)  
    aut.click()

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
start_y = 258
x_offset = 42
y_offset = 37
num_rows = 7
num_cols = 4


def herbclean():
        
    while True:
        herb()
        click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
            


