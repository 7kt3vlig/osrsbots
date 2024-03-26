import cv2
import numpy as np
import pyautogui
import time 

# Load the template image (guard) and convert it to grayscale
template = cv2.imread('guard.png', cv2.IMREAD_GRAYSCALE)

while True:
    try:
        # Capture the screen
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

        # Set a threshold to filter out weak matches
        threshold = 0.5
        loc = np.where(res >= threshold)

        # If any matches found, click on the center of the first match
        if loc[0].size > 0:
            y, x = loc[0][0] + template.shape[0] // 2, loc[1][0] + template.shape[1] // 2
            pyautogui.click(x + 1 , y + 7)
            
            print("Guard detected at:", x, y)
            
            time.sleep(20)
        else:
            print("Guard not detected.")

    except Exception as e:
        print("Error:", e)

    # Display the result (optional)
    # cv2.imshow('Object Detection', screenshot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



