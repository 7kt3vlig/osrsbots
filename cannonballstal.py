import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random
import PIL.ImageGrab






def ta():
    aut.PAUSE=0.05
    aut.moveTo(1433, 357) 
    aut.click()
    time.sleep(12)
    aut.moveTo(1379, 402)  
    aut.click()
    time.sleep(6)
  

# --- DINA INSTÄLLNINGAR ---

#kamera 710 zoom
SCAN_AREA = (1500, 215, 1630, 364) 
CLICK_POINT_A = (1414, 225) #hälen av främre foten
CLICK_POINT_B = (1474, 225)

# RGB-färg för ROSA (Magenta: 255 Röd, 0 Grön, 255 Blå)
TARGET_COLOR = (255, 0, 255) 
TOLERANCE = 50  # Ökad tolerans för att fånga olika nyanser av rosa

# --- STABILISERINGS-INSTÄLLNINGAR ---
MIN_PIXELS = 30      # Kräver minst 30 pixlar rosa
CONFIRM_STEPS = 1    # Måste se rosa 3 gånger i rad för att klicka

färg_fanns_förut = None 
räknare = 0

def kolla_färg(img, target, tol):
    count = 0
    tr, tg, tb = target
    for r, g, b in img.getdata():
        # Kollar om pixeln är tillräckligt nära Rosa
        if abs(r - tr) <= tol and abs(g - tg) <= tol and abs(b - tb) <= tol:
            count += 1
    return count >= MIN_PIXELS

print("Scriptet körs med färg: ROSA. Tryck Ctrl+C för att stoppa.")

try:
    while True:
        img = PIL.ImageGrab.grab(bbox=SCAN_AREA)
        färg_finns_nu = kolla_färg(img, TARGET_COLOR, TOLERANCE)

        # Logik för att klicka endast vid stabil förändring
        if färg_finns_nu != färg_fanns_förut:
            räknare += 1
            if räknare >= CONFIRM_STEPS:
                if färg_finns_nu:
                    print(f"Rosa bekräftad. Klickar A @ {CLICK_POINT_A}")
                    aut.click(CLICK_POINT_A)
                    aut.click(CLICK_POINT_A)
                    färg_fanns_förut = True
                else:
                    print(f"Rosa borta. Klickar B @ {CLICK_POINT_B}")
                    aut.click(CLICK_POINT_B)
                    aut.click(CLICK_POINT_B)
                    färg_fanns_förut = False
                räknare = 0
        else:
            räknare = 0 

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nAvslutat.")