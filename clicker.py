import pyautogui as aut
import time




click_interval = 0.01   # seconds between clicks
total_duration = 70   # total time to click (seconds)

start_time = time.time()

while time.time() - start_time < total_duration:
    aut.click()
    time.sleep(click_interval)