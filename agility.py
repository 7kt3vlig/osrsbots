import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 
import random
import time 
import math  



def slow():

    aut.moveTo(607, 234)
    aut.click()
    time.sleep(14)

    aut.moveTo(759, 199)
    aut.click()
    time.sleep(12)

    aut.moveTo(736, 156)
    aut.click()
    time.sleep(10)

    aut.moveTo(765, 204)
    aut.click()
    time.sleep(16)

    aut.moveTo(883, 266)
    aut.click()
    time.sleep(7)

    aut.moveTo(1040, 189)
    aut.click()
    time.sleep(15)

    aut.moveTo(1021, 159)
    aut.click()
    time.sleep(13)

    aut.moveTo(842, 124)
    aut.click()
    time.sleep(9)

    aut.moveTo(842, 138)
    aut.click()
    time.sleep(8)



def fast():
    aut.moveTo(607, 234)
    aut.click()
    time.sleep(9)

    aut.moveTo(759, 199)
    aut.click()
    time.sleep(9)

    aut.moveTo(736, 156)
    aut.click()
    time.sleep(7)

    aut.moveTo(765, 204)
    aut.click()
    time.sleep(12)

    aut.moveTo(883, 266)
    aut.click()
    time.sleep(5)

    aut.moveTo(1040, 189)
    aut.click()
    time.sleep(11)

    aut.moveTo(1021, 159)
    aut.click()
    time.sleep(10)

    aut.moveTo(842, 124)
    aut.click()
    time.sleep(4)

    aut.moveTo(842, 138)
    aut.click()
    time.sleep(5)


def togglerun():
    aut.moveTo(1144, 146)
    time.sleep(1)
    aut.click()
    
def falador():
    aut.moveTo(918, 112) #1
    aut.click()
    time.sleep(5)

    aut.moveTo(890, 180)#2
    aut.click()
    time.sleep(8)

    aut.moveTo(870, 133)#3
    aut.click()
    time.sleep(10)

    aut.moveTo(814, 171)#4
    aut.click()
    time.sleep(3)

    aut.moveTo(785, 194)#5
    aut.click()
    time.sleep(4)

    aut.moveTo(746, 190)#6
    aut.click()
    time.sleep(10)

    aut.moveTo(810, 207)#7
    aut.click()
    time.sleep(5)

    aut.moveTo(811, 199)#8
    aut.click()
    time.sleep(3)

    aut.moveTo(809, 241)#9
    aut.click()
    time.sleep(3.5)

    aut.moveTo(824, 226)#10
    aut.click()
    time.sleep(3)

    aut.moveTo(851, 300)#11
    aut.click()
    time.sleep(5)

    aut.moveTo(900, 195)#12
    aut.click()
    time.sleep(3.5)

    aut.moveTo(905, 203)#13
    aut.click()
    time.sleep(5)







########################################################################
def prifdinnas(): # kamera 129 som falador 
    # 1
    aut.moveTo(1030, 195)
    aut.click()
    time.sleep(random.uniform(8, 11))

    # 2
    aut.moveTo(870, 250)
    aut.click()
    time.sleep(random.uniform(14, 20))

    # 3
    aut.moveTo(850, 170)
    aut.click()
    time.sleep(random.uniform(6, 11))

    # 4
    aut.moveTo(840, 155)
    aut.click()
    time.sleep(random.uniform(5, 11))

    # 5
    aut.moveTo(840, 185)
    aut.click()
    time.sleep(random.uniform(5, 11))

    # 6
    aut.moveTo(850, 135)
    aut.click()
    time.sleep(random.uniform(5, 11))

    # 7
    aut.moveTo(765, 240)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 8
    aut.moveTo(790, 200)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 9
    aut.moveTo(825, 175)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 10
    aut.moveTo(805, 165)
    aut.click()
    time.sleep(random.uniform(9, 11))

    # 11
    aut.moveTo(880, 175)
    aut.click()
    time.sleep(random.uniform(8, 11))

    # 12
    aut.moveTo(815, 130)
    aut.click()
    time.sleep(random.uniform(9, 16))

    # 13 (Väntetid efter sista klicket innan loopen börjar om)
    time.sleep(random.uniform(1, 10))



# 2
# 3
# 4 
# 5
# 6 
# 7 - då blir 8 1439, 146 
# 8
# 9
# 10
# 11 - dp blir 12 1370 136 



def prifdinnas2(): #kamera 129 som falador 
    aut.moveTo(1605, 195) #1
    aut.click()
    time.sleep(random.uniform(7,8))

    aut.moveTo(1450, 250)#2
    aut.click()
    time.sleep(random.uniform(14,15))

    aut.moveTo(1430, 170)#3
    aut.click()
    time.sleep(random.uniform(6,7))

    aut.moveTo(1415, 155)#4
    aut.click()
    time.sleep(5)

    aut.moveTo(1415, 185)#5
    aut.click()
    time.sleep(5)

    aut.moveTo(1430, 135)#6
    aut.click()
    time.sleep(random.uniform(5,7))

    aut.moveTo(1340, 240)#7
    aut.click()
    time.sleep(random.uniform(9, 11))

    aut.moveTo(1370,200)#8
    aut.click()
    time.sleep(random.uniform(9, 11))

    aut.moveTo(1400, 175)#9
    aut.click()
    time.sleep(random.uniform(9, 11))

    aut.moveTo(1385, 165)#10
    aut.click()
    time.sleep(random.uniform(9, 11))

    aut.moveTo(1460, 175)#11
    aut.click()
    time.sleep(random.uniform(8, 11))

    aut.moveTo(1393, 130)#12
    aut.click()
    time.sleep(random.uniform(9,10))


def smart_click(x, y):
    # Försök hitta rosa först
    found_pink = scan_and_interact()
    
    # Om ingen rosa hittades, klicka på de fasta koordinaterna
    if not found_pink:
        print(f"Inget rosa, klickar på backup: ({x}, {y})")
        aut.click(x, y)
        aut.click(x, y)

def prifdinnas3(): #kamera 129 som falador 

    smart_click(1030, 195)
    time.sleep(8)

    smart_click(870, 250)
    time.sleep(14)

    smart_click(850, 170)
    time.sleep(6)

    smart_click(840, 155)
    time.sleep(5)

    smart_click(840, 185)
    time.sleep(5)

    smart_click(850, 135)
    time.sleep(5)

    smart_click(765, 240)
    time.sleep(9)

    smart_click(790,200)
    time.sleep(9)

    smart_click(825, 175)
    time.sleep(9)

    smart_click(805, 165)
    time.sleep(9)

    smart_click(880, 175)
    time.sleep(8)

    smart_click(815, 130)
    time.sleep(9)


def ardy(): #kamera 129 som falador 
    aut.moveTo(1480, 185) #1
    aut.click()
    time.sleep(5.5)

    aut.moveTo(1410, 95)#2
    aut.click()
    time.sleep(9)

    aut.moveTo(1360, 200)#3
    aut.click()
    time.sleep(7.5)

    aut.moveTo(1370, 210)#4
    aut.click()
    time.sleep(3.5)

    aut.moveTo(1415, 275)#5
    aut.click()
    time.sleep(5)

    aut.moveTo(1470, 350)#6
    aut.click()
    time.sleep(7)

    aut.moveTo(1420, 210)#7
    aut.click()
    time.sleep(11)



def tabild():
    try:
        screenshot = ImageGrab.grab(bbox=(581, 26, 1093, 361))#847, 214, 861, 228)
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        
        # Load the template image
        template = cv.imread("pillar.png")
        
        # Perform template matching
        result = cv.matchTemplate(screenshot, template, method=cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print("max val = %s" % str (max_val), "max loc = %s" % str (max_loc))
    except Exception as e:
        print("Error:", e)
    finally:
        try:
            os.remove("sample.png")
            print("File 'sample.png' removed successfully.")
        except Exception as e:
            print("Error while removing file:", e)
        if max_val >= 0.9:
            aut.moveTo(836, 169)
            time.sleep(1)
            aut.click()
            time.sleep(3)
        elif max_val >= 0.8:
            aut.moveTo(836, 184)
            time.sleep(1)
            aut.click()
            time.sleep(3)
        else:
            pass

'''
while True:


    for i in range (2):
        slow()

    togglerun()
    for i in range (10):
        fast()

    togglerun()
'''
#kamera 102, 129 
#en runda tar 68-69 sekunder
# for i in range(360):
#     tabild()
#     falador()


# while True:

#     prifdinnas2()











RED_LOWER = np.array([160, 100, 100])
RED_UPPER = np.array([180, 255, 255])
MONITOR_REGION = (1150, 19, 1671, 366) 

def scan_and_interact2():

    
    # Screenshot på dina förinställda koordinater
    screenshot = ImageGrab.grab(bbox=MONITOR_REGION)

    frame = np.array(screenshot)
    frame_bgr = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
    
    # 2. Använd den gröna masken istället för den rosa
    mask = cv.inRange(hsv, RED_LOWER, RED_UPPER)
    
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        M = cv.moments(largest_contour)
        if M["m00"] != 0:
            # Räkna ut lokalt center i bilden
            local_x = int(M["m10"] / M["m00"])
            local_y = int(M["m01"] / M["m00"])
            
            # Addera startpunkten för att få rätt skärmplats
            global_x = local_x + MONITOR_REGION[0]
            global_y = local_y + MONITOR_REGION[1]
            
            print(f"Hittade neongrönt! Klickar på: ({global_x}, {global_y})")
            aut.click(global_x, global_y + 10)
            return True
    
    return False

# --- Inställningar ---
# Definiera det område du vill bevaka: (left, top, width, height)
# Tips: Använd pyautogui.position() för att hitta koordinaterna.
MONITOR_REGION = (1150, 19, 1671, 361) 

# Definiera "Rosa" i HSV-färgrymd (Hue, Saturation, Value)
# Dessa värden täcker de flesta starkrosa nyanser.
PINK_LOWER = np.array([140, 50, 50])
PINK_UPPER = np.array([170, 255, 255])

def scan_and_interact():
    # 1. Ta screenshot EXAKT på dina koordinater
    screenshot = ImageGrab.grab(bbox=MONITOR_REGION)

    frame = np.array(screenshot)
    frame_bgr = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, PINK_LOWER, PINK_UPPER)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        M = cv.moments(largest_contour)
        if M["m00"] != 0:
            # 2. Räkna ut lokalt center i bilden
            local_x = int(M["m10"] / M["m00"])
            local_y = int(M["m01"] / M["m00"])
            
            # 3. Addera startpunkten (583, 36) för att få rätt skärmplats
            global_x = local_x + MONITOR_REGION[0]
            global_y = local_y + MONITOR_REGION[1]
            
            print(f"Hittade rosa! Klickar på: ({global_x}, {global_y})")
            aut.click(global_x, global_y + 10)
            return True
    
    return False





# while True:

#     #1
#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(8)



#     #2

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(14)


#     #3

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(6)


#     #4

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(5)




#     #5

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(5)



#     #6

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(5)



#     #7

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(9)



#     #8

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(9)




#     #9

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(9)



    
#     #10

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(9)



#     #11

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(8)



#     #12

#     if scan_and_interact():
#         # Om rosa hittades, hoppa direkt till nästa iteration i for-loopen
#         time.sleep(5)
#         continue 
    
#     # Om rosa INTE hittades, kör grön scanning
#     scan_and_interact2()
#     time.sleep(9)











# # --- Inställningar ---
# MONITOR_REGION = (1150, 19, 1671, 361) 
# TARGET_X, TARGET_Y = 1415, 200  # Punkten vi vill vara nära

# YELLOW_LOWER = np.array([25, 100, 100])
# YELLOW_UPPER = np.array([35, 255, 255])

# # Röda gränser (Två masker för att täcka hela spektrumet)
# RED_LOWER1, RED_UPPER1 = np.array([0, 100, 100]), np.array([10, 255, 255])
# RED_LOWER2, RED_UPPER2 = np.array([160, 100, 100]), np.array([180, 255, 255])

# def scan_rosa():
#     screenshot = ImageGrab.grab(bbox=MONITOR_REGION)
#     frame = np.array(screenshot)
#     hsv = cv.cvtColor(cv.cvtColor(frame, cv.COLOR_RGB2BGR), cv.COLOR_BGR2HSV)
#     mask = cv.inRange(hsv, YELLOW_LOWER, YELLOW_UPPER)
#     contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#     if contours:
#         largest = max(contours, key=cv.contourArea)
#         M = cv.moments(largest)
#         if M["m00"] != 0:
#             gx = int(M["m10"] / M["m00"]) + MONITOR_REGION[0]
#             gy = int(M["m01"] / M["m00"]) + MONITOR_REGION[1]
#             print(f"Hittade Rosa! Klickar på: ({gx}, {gy})")
#             aut.click(gx, gy )
#             aut.click(gx, gy )
#             return True
#     return False

# def scan_rod_narmast():
#     screenshot = ImageGrab.grab(bbox=MONITOR_REGION)
#     frame = np.array(screenshot)
#     hsv = cv.cvtColor(cv.cvtColor(frame, cv.COLOR_RGB2BGR), cv.COLOR_BGR2HSV)
    
#     mask = cv.inRange(hsv, RED_LOWER1, RED_UPPER1) | cv.inRange(hsv, RED_LOWER2, RED_UPPER2)
#     contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#     best_point = None
#     min_dist = float('inf')

#     for cnt in contours:
#         if cv.contourArea(cnt) < 5: # Ignorera brus/småpixlar
#             continue
            
#         M = cv.moments(cnt)
#         if M["m00"] != 0:
#             # Räkna ut global position
#             gx = int(M["m10"] / M["m00"]) + MONITOR_REGION[0]
#             gy = int(M["m01"] / M["m00"]) + MONITOR_REGION[1]
            
#             # Räkna ut avståndet till målet (1415, 200)
#             dist = math.sqrt((gx - TARGET_X)**2 + (gy - TARGET_Y)**2)
            
#             if dist < min_dist:
#                 min_dist = dist
#                 best_point = (gx, gy)

#     if best_point:
#         print(f"Hittade röd närmast målet! Avstånd: {int(min_dist)}. Klickar på: {best_point}")
#         aut.click(best_point[0], best_point[1] )
#         aut.click(best_point[0], best_point[1] )
#         return True
#     return False

# delays = [8, 14, 6, 5, 5, 5, 9, 9, 9, 9, 8, 9]

# print("Startar skanning (Prioriterar röd närmast 1415, 200)...")

# while True:
#     for i, wait_time in enumerate(delays):
#         print(f"Steg {i+1}/12")
#         if scan_rosa():
#             time.sleep(5)
#         else:
#             scan_rod_narmast()
#             time.sleep(wait_time)










# # --- Inställningar ---
# MONITOR_REGION = (1150, 19, 1671, 361) 
# TARGET_X, TARGET_Y = 1415, 200  # Punkten vi vill vara nära

# # Röda gränser (Två masker för att täcka hela spektrumet i OpenCV)
# RED_LOWER1 = np.array([0, 100, 100])
# RED_UPPER1 = np.array([10, 255, 255])
# RED_LOWER2 = np.array([160, 100, 100])
# RED_UPPER2 = np.array([180, 255, 255])

# def scan_rod_narmast():
#     # Ta screenshot
#     screenshot = ImageGrab.grab(bbox=MONITOR_REGION)
#     frame = np.array(screenshot)
    
#     # Konvertera till HSV
#     frame_bgr = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
#     hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
    
#     # Skapa kombinerad röd mask
#     mask = cv.inRange(hsv, RED_LOWER1, RED_UPPER1) | cv.inRange(hsv, RED_LOWER2, RED_UPPER2)
#     contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#     best_point = None
#     min_dist = float('inf')

#     for cnt in contours:
#         if cv.contourArea(cnt) < 5: # Filtrera bort småbrus
#             continue
            
#         M = cv.moments(cnt)
#         if M["m00"] != 0:
#             # Räkna ut global position på skärmen
#             gx = int(M["m10"] / M["m00"]) + MONITOR_REGION[0]
#             gy = int(M["m01"] / M["m00"]) + MONITOR_REGION[1]
            
#             # Räkna ut avståndet till 1415, 200
#             dist = math.sqrt((gx - TARGET_X)**2 + (gy - TARGET_Y)**2)
            
#             if dist < min_dist:
#                 min_dist = dist
#                 best_point = (gx, gy)

#     if best_point:
#         print(f"Hittade röd! Avstånd: {int(min_dist)} px. Klickar på: {best_point}")
#         aut.click(best_point[0], best_point[1])
#         aut.click(best_point[0], best_point[1])
#         return True
    
#     print("Hittade ingen röd färg i området.")
#     return False

# # Dina väntetider för de 12 stegen
# delays = [8, 14, 6, 5, 5, 5, 9, 9, 9, 9, 8, 9]

# print(f"Startar skanning efter RÖTT närmast ({TARGET_X}, {TARGET_Y})...")

# while True:
#     for i, wait_time in enumerate(delays):
#         print(f"Steg {i+1}/12")
        
#         # Kör enbart röd skanning
#         scan_rod_narmast()
        
#         # Vänta den tid som är satt för detta steg
#         time.sleep(wait_time)




while True:
    # prifdinnas2()
    ardy()