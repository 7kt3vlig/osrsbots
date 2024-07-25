import pyautogui 
import time 



def autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset):
    for i in range(num_cols):
        x = start_x + i * x_offset
        for j in range(num_rows):
            y = start_y + j * y_offset
            pyautogui.keyDown("shift")
            pyautogui.moveTo(x, y)
            pyautogui.click()
            pyautogui.keyUp("shift")

# Define the starting point and offsets
start_x = 585
start_y = 258
x_offset = 42
y_offset = 37
num_rows = 7
num_cols = 4

while True:
    for i in range (28):
        pyautogui.moveTo(310, 269)
        pyautogui.click()
        time.sleep(4.2)

    autodropperscreen1(start_x, start_y, num_rows, num_cols, x_offset, y_offset)
