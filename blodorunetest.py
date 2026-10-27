import tkinter as tk
import threading
import pyautogui as aut
import numpy as np
import cv2 as cv
import time


## ALLMÄNA REGLER
## ZOOMA UT MAX, HA COMPASSEN CENTRALT - THATS IT 

# -----------------------------
# PINK SHAPE DETECTION (ONE SCAN)
# -----------------------------

def minepink():
    top_left = (1399, 120)
    bottom_right = (1420, 150)

    try:
        screenshot = aut.screenshot(
            region=(
                top_left[0], top_left[1],
                bottom_right[0] - top_left[0],
                bottom_right[1] - top_left[1]
            )
        )

        screenshot_cv = cv.cvtColor(
            np.array(screenshot), cv.COLOR_RGB2BGR
        )
        hsv = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2HSV)

        lower_pink = np.array([140, 50, 50])
        upper_pink = np.array([179, 255, 255])
        mask = cv.inRange(hsv, lower_pink, upper_pink)

        kernel = np.ones((3, 3), np.uint8)
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        contours, _ = cv.findContours(
            mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )
        contours = [c for c in contours if cv.contourArea(c) >= 3]

        if not contours:
            print("No pink shape found.")
            return False

        largest = max(contours, key=cv.contourArea)
        M = cv.moments(largest)

        if M["m00"] == 0:
            return False

        click_x = top_left[0] + int(M["m10"] / M["m00"])
        click_y = top_left[1] + int(M["m01"] / M["m00"])

        print(f"Pink shape found at ({click_x}, {click_y})")
        aut.click(click_x, click_y)
        aut.click(click_x, click_y)
        time.sleep(10)
        aut.moveTo(1273,176)
        aut.click()
        time.sleep(20)
        return True

    except Exception as e:
        print(f"Pink finder error: {e}")
        return False

def minepink2():
    top_left = (1464, 130)
    bottom_right = (1484, 146)

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
        hsv = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2HSV)

        lower_pink = np.array([140, 50, 50])
        upper_pink = np.array([179, 255, 255])
        mask = cv.inRange(hsv, lower_pink, upper_pink)

        kernel = np.ones((3, 3), np.uint8)
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        contours, _ = cv.findContours(
            mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )
        contours = [c for c in contours if cv.contourArea(c) >= 3]

        if not contours:
            print("No pink shape found in region 2.")
            return False

        largest = max(contours, key=cv.contourArea)
        M = cv.moments(largest)

        if M["m00"] == 0:
            return False

        click_x = top_left[0] + int(M["m10"] / M["m00"])
        click_y = top_left[1] + int(M["m01"] / M["m00"])

        print(f"Pink shape 2 found at ({click_x}, {click_y})")
        aut.click(click_x, click_y)
        aut.click(click_x, click_y)
        time.sleep(20)
        aut.moveTo(1458, 212)
        aut.click()
        return True

    except Exception as e:
        print(f"Pink finder 2 error: {e}")
        return False
# -----------------------------
# CHISELESSENSE
# -----------------------------

def chiselessense():
    for i in range(27):
        aut.PAUSE = 0.05
        aut.moveTo(1860, 475)
        aut.click()
        aut.moveTo(1825, 475)
        aut.click()

    print("Chiselessense finished.")


# -----------------------------
# CHECK MINING STATUS
# -----------------------------

def check_mining_status():
    top_left = (1183, 55)
    bottom_right = (1261, 76)
    threshold = 0.70

    try:
        screenshot = aut.screenshot(
            region=(
                top_left[0], top_left[1],
                bottom_right[0] - top_left[0],
                bottom_right[1] - top_left[1]
            )
        )
        screenshot_cv = cv.cvtColor(
            np.array(screenshot), cv.COLOR_RGB2BGR
        )
    except Exception as e:
        print(f"Screenshot error: {e}")
        return None

    active_template = cv.imread("activemining.png")
    not_mining_template = cv.imread("notmining.png")

    if active_template is None or not_mining_template is None:
        print("Could not load mining template images.")
        return None

    scores = {}

    for name, template in {
        "ACTIVE MINING": active_template,
        "NOT MINING": not_mining_template
    }.items():
        if (
            template.shape[0] > screenshot_cv.shape[0]
            or template.shape[1] > screenshot_cv.shape[1]
        ):
            print(f"{name}: template is too large.")
            continue

        result = cv.matchTemplate(
            screenshot_cv, template, cv.TM_CCOEFF_NORMED
        )
        _, max_val, _, _ = cv.minMaxLoc(result)
        scores[name] = max_val
        print(f"{name}: {max_val:.2%}")

    if not scores:
        return None

    best_match = max(scores, key=scores.get)

    if scores[best_match] >= threshold:
        print(f"Detected: {best_match}")
        return best_match

    print("Mining status unclear.")
    return None


# -----------------------------
# MINE ESSENCE (YELLOW SHAPE)
# -----------------------------

def mineessence():
    top_left = (1313, 104)
    bottom_right = (1580, 311)

    try:
        screenshot = aut.screenshot(
            region=(
                top_left[0], top_left[1],
                bottom_right[0] - top_left[0],
                bottom_right[1] - top_left[1]
            )
        )
        screenshot_cv = cv.cvtColor(
            np.array(screenshot), cv.COLOR_RGB2BGR
        )
        hsv = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2HSV)

        lower_yellow = np.array([10, 50, 50])
        upper_yellow = np.array([45, 255, 255])
        mask = cv.inRange(hsv, lower_yellow, upper_yellow)

        kernel = np.ones((3, 3), np.uint8)
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

        contours, _ = cv.findContours(
            mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )
        contours = [c for c in contours if cv.contourArea(c) >= 30]

        if not contours:
            print("No yellow shape found.")
            return False

        largest = max(contours, key=cv.contourArea)
        M = cv.moments(largest)

        if M["m00"] == 0:
            return False

        click_x = top_left[0] + int(M["m10"] / M["m00"])
        click_y = top_left[1] + int(M["m01"] / M["m00"])

        print(f"Yellow shape found: ({click_x}, {click_y})")
        aut.moveTo(click_x, click_y, duration=0.2)
        aut.click()
        return True

    except Exception as e:
        print(f"mineessence error: {e}")
        return False

# -----------------------------
# CHECK FOR FULL INVENTORY
# -----------------------------

def check_full_inventory():
    top_left = (1193, 385)
    bottom_right = (1580, 500)
    threshold = 0.80

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

        template = cv.imread("fullinventorymining.png")

        if template is None:
            print("Could not load fullinventorymining.png.")
            return False

        if (
            template.shape[0] > screenshot_cv.shape[0]
            or template.shape[1] > screenshot_cv.shape[1]
        ):
            print("Inventory template is too large for the region.")
            return False

        result = cv.matchTemplate(
            screenshot_cv,
            template,
            cv.TM_CCOEFF_NORMED
        )

        _, max_val, _, _ = cv.minMaxLoc(result)

        print(f"Full inventory match: {max_val:.2%}")

        if max_val >= threshold:
            print("FULL INVENTORY DETECTED!")
            return True

        return False

    except Exception as e:
        print(f"Full inventory detection error: {e}")
        return False

# -----------------------------
# BACKGROUND TASK CONTROL
# -----------------------------

monitor_running = threading.Event()


def start_chiselessense():
    threading.Thread(target=chiselessense, daemon=True).start()


def mining_monitor():
    print("Mining monitor started.")

    while monitor_running.is_set():

        # Check inventory first
        if check_full_inventory():
            print("Inventory full. Stopping mining monitor.")
            monitor_running.clear()

            # Update GUI safely from the Tkinter main thread
            root.after(
                0,
                lambda: start_button.config(
                    text="Start Mining Monitor"
                )
            )
            break

        # Check normal mining status
        status = check_mining_status()

        if not monitor_running.is_set():
            break

        if status == "NOT MINING":
            print("Not mining. Looking for essence.")
            mineessence()

        elif status == "ACTIVE MINING":
            print("Already mining.")

        else:
            print("Unable to determine status.")

        # Wait 5 seconds, checking for a stop request
        for _ in range(50):
            if not monitor_running.is_set():
                break
            time.sleep(0.1)

    print("Mining monitor stopped.")


def toggle_monitor():
    if monitor_running.is_set():
        monitor_running.clear()
        start_button.config(text="Start Mining Monitor")
    else:
        monitor_running.set()
        start_button.config(text="Stop Mining Monitor")
        threading.Thread(target=mining_monitor, daemon=True).start()


def run_pink_finder():
    # One scan for each button press
    threading.Thread(target=minepink, daemon=True).start()


# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()
root.title("Mining Control Panel")
root.geometry("360x350")
root.resizable(False, False)

tk.Label(
    root,
    text="Mining Control Panel",
    font=("Arial", 16, "bold")
).pack(pady=15)

tk.Button(
    root,
    text="Run Chiselessense",
    width=25,
    height=2,
    command=start_chiselessense
).pack(pady=5)

start_button = tk.Button(
    root,
    text="Start Mining Monitor",
    width=25,
    height=2,
    command=toggle_monitor
)
start_button.pack(pady=5)

pink_button = tk.Button(
    root,
    text="Find Pink Shape",
    width=25,
    height=2,
    command=run_pink_finder
)
pink_button.pack(pady=5)

pink_button2 = tk.Button(
    root,
    text="Find Pink Shape 2",
    width=25,
    height=2,
    command=lambda: threading.Thread(
        target=minepink2,
        daemon=True
    ).start()
)
pink_button2.pack(pady=5)


def close_app():
    monitor_running.clear()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()