import pyautogui as aut
import time 


def click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            aut.moveTo(x, y)
            aut.click()
            time.sleep(85)
            aut.click()
            time.sleep(85)
            aut.click()
            time.sleep(85)
            aut.click()
            time.sleep(85)

# aut.moveTo(585, 180)
# aut.click()
# time.sleep(65)     

# Define the starting point and offsets
start_x = 585
start_y = 258
x_offset = 42
y_offset = 37
num_rows = 7
num_cols = 4


click_positions(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
