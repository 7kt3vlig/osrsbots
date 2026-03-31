import pyautogui as aut
import numpy as np
import cv2 as cv
import time

aut.PAUSE = 0

# Load both templates in color
template1 = cv.imread("lapp.png", cv.IMREAD_COLOR)
template2 = cv.imread("lapp2.png", cv.IMREAD_COLOR)

if template1 is None or template2 is None:
    print("Error loading one or both templates. Check file paths.")
    exit()

def restart():
    aut.moveTo(1625, 715)
    time.sleep(0.2)
    aut.click()
    time.sleep(1)

def match_template(screenshot_cv, template, label="Template"):
    result = cv.matchTemplate(screenshot_cv, template, cv.TM_SQDIFF_NORMED)
    min_val, _, min_loc, _ = cv.minMaxLoc(result)
    print(f"[{label}] Match score (lower is better): {min_val:.6f}")
    return min_val, min_loc

def click_if_match(template, template_label):
    # Define region to capture
    top_left = (818, 319)
    bottom_right = (1259, 993)

    try:
        screenshot = aut.screenshot(region=(
            top_left[0], top_left[1],
            bottom_right[0] - top_left[0],
            bottom_right[1] - top_left[1]
        ))
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return False

    min_val, min_loc = match_template(screenshot_cv, template, template_label)

    # Adjust this threshold as needed
    if min_val <= 0.04:
        center_x = min_loc[0] + template.shape[1] // 2
        center_y = min_loc[1] + template.shape[0] // 2
        screen_x = top_left[0] + center_x
        screen_y = top_left[1] + center_y

        print(f"[{template_label}] Match found. Clicking at: ({screen_x}, {screen_y})")
        aut.moveTo(screen_x, screen_y)
        aut.click()
        return True
    else:
        print(f"[{template_label}] No match found above threshold.")
        return False

# Main loop
while True:
    matched = click_if_match(template1, "lapp.png")
    