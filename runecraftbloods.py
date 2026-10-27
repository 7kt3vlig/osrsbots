import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import win32 
import numpy as np
import random


    #essence to essence fragments 

def chiselessense():
    for i in range(27):
            aut.PAUSE= 0.05
            aut.moveTo(1860, 475) #
            aut.click()
            aut.moveTo(1825, 475) #
            aut.click()


import cv2 as cv
import pyautogui as aut
import numpy as np

def check_mining_status():
    top_left = (1183, 55)
    bottom_right = (1261, 76)
    threshold = 0.70

    # Capture the specified screen region
    try:
        screenshot = aut.screenshot(
            region=(
                top_left[0],
                top_left[1],
                bottom_right[0] - top_left[0],
                bottom_right[1] - top_left[1]
            )
        )
        screenshot_cv = cv.cvtColor(
            np.array(screenshot), cv.COLOR_RGB2BGR
        )
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None

    # Load both template images
    active_template = cv.imread("activemining.png")
    not_mining_template = cv.imread("notmining.png")

    if active_template is None:
        print("Could not load activemining.png")
        return None

    if not_mining_template is None:
        print("Could not load notmining.png")
        return None

    # Compare the screenshot against both templates
    templates = {
        "ACTIVE MINING": active_template,
        "NOT MINING": not_mining_template
    }

    scores = {}

    for name, template in templates.items():
        # Template must fit inside the captured screenshot
        if (template.shape[0] > screenshot_cv.shape[0] or
                template.shape[1] > screenshot_cv.shape[1]):
            print(f"{name}: Template is larger than the scan region.")
            continue

        result = cv.matchTemplate(
            screenshot_cv, template, cv.TM_CCOEFF_NORMED
        )

        _, max_val, _, max_loc = cv.minMaxLoc(result)
        scores[name] = max_val

        print(f"{name} match score: {max_val:.2%}")

    # Determine which template matches
    if not scores:
        return None

    best_match = max(scores, key=scores.get)
    best_score = scores[best_match]

    if best_score >= threshold:
        print(f"Detected: {best_match} ({best_score:.2%})")
        return best_match
    else:
        print(f"No match found above {threshold:.0%} threshold.")
        return None


# Run the check
status = check_mining_status()
print("Mining status:", status)

def mineessence():
    top_left = (1313, 104)
    bottom_right = (1580, 311)

    try:
        # Capture the screen region
        screenshot = aut.screenshot(
            region=(
                top_left[0],
                top_left[1],
                bottom_right[0] - top_left[0],
                bottom_right[1] - top_left[1]
            )
        )

        screenshot_cv = cv.cvtColor(
            np.array(screenshot), cv.COLOR_RGB2BGR
        )

        # Convert to HSV
        hsv = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2HSV)

        # Wider yellow hue range
        lower_yellow = np.array([10, 50, 50])
        upper_yellow = np.array([45, 255, 255])

        # Detect yellow pixels
        mask = cv.inRange(hsv, lower_yellow, upper_yellow)

        # Remove noise and fill small gaps
        kernel = np.ones((3, 3), np.uint8)
        mask = cv.morphologyEx(
            mask, cv.MORPH_OPEN, kernel
        )
        mask = cv.morphologyEx(
            mask, cv.MORPH_CLOSE, kernel
        )

        # Find yellow shapes
        contours, _ = cv.findContours(
            mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        # Ignore small shapes
        contours = [
            c for c in contours
            if cv.contourArea(c) >= 30
        ]

        if not contours:
            print("No yellow shape found.")
            return False

        # Find the largest yellow shape
        largest_contour = max(contours, key=cv.contourArea)

        # Calculate the center of the shape
        M = cv.moments(largest_contour)

        if M["m00"] == 0:
            print("Could not calculate the center.")
            return False

        center_x = int(M["m10"] / M["m00"])
        center_y = int(M["m01"] / M["m00"])

        # Convert to absolute screen coordinates
        click_x = top_left[0] + center_x
        click_y = top_left[1] + center_y

        print(f"Yellow shape found at ({click_x}, {click_y})")

        # Click the center of the yellow shape
        aut.moveTo(click_x, click_y, duration=0.2)
        aut.click()

        return True

    except Exception as e:
        print(f"Error in mineessence(): {e}")
        return False



# chiselessense()

while True:
    status = check_mining_status()

    if status == "NOT MINING":
        mineessence()

    time.sleep(5)


