import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 

# print("checking dodgyneck..")

# # Define the region of interest (ROI) coordinates
# roi_top_left = (9, 32)
# roi_bottom_right = (520, 366)

# # Define a list of template image filenames
# template_filenames = ["paladin.png", "paladin1.png", "paladin2.png", "paladin3.png"]

# while True:
#     for template_filename in template_filenames:
#         screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
#                                             roi_bottom_right[0] - roi_top_left[0], 
#                                             roi_bottom_right[1] - roi_top_left[1]))

#         # Convert the screenshot to OpenCV format (BGR)
#         screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

#         # Convert the filtered image to grayscale
#         grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

#         # Load the template image
#         template = cv.imread(template_filename, cv.IMREAD_GRAYSCALE)

#         # Blur both the grayscale image and the template
#         blur = cv.blur(grayscale_img, (3,3))
#         blur1 = cv.blur(template, (3,3))

#         # Apply Canny edge detection to both images
#         canny = cv.Canny(blur, 125, 175)
#         canny1 = cv.Canny(blur1, 125, 175)

#         # Perform template matching
#         result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

#         # Define a threshold for the match
#         threshold = 0.2

#         # Get the location of the best match
#         min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

#         # Calculate the center of the max location
#         template_height, template_width = template.shape
#         center_x = max_loc[0] + template_width // 2
#         center_y = max_loc[1] + template_height // 2

#         # Convert the center coordinates to the actual screen location
#         center_screen = (center_x + roi_top_left[0], center_y + roi_top_left[1])

#         # Print the template filename, maximum value, and its center screen location
#         print("Template:", template_filename)
#         print("Max value:", max_val)
#         print("Max center location (on screen):", center_screen)
#         print()

#         # If the maximum value exceeds the threshold, click 18 pixels to the right and 29 pixels down from the center screen location
#         if max_val >= threshold:
#             aut.click(center_screen[0] + 18, center_screen[1] + 29)

#         # Add a short delay before moving to the next template
#         time.sleep(1)


# while True:

#     aut.moveTo(1415, 250) #shoikeepr
#     aut.click(button="right")
#     time.sleep(1)
#     aut.moveRel(0 , +45, duration=0.2)
#     time.sleep(0.5)
#     aut.click()
#     time.sleep(0.5)


#     aut.moveTo(1415, 250) #shoikeepr
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1477, 330) #valj 1
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1340, 109) #köp alla
#     for i in range(28):
                
#         aut.click()
#         time.sleep(0.1)

#     aut.press("esc")
#     time.sleep(1)

#     aut.moveTo(1818, 475) #börja crafta
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1860, 475) #börja crafta
#     aut.click()
#     time.sleep(1)
#     aut.press("space")
#     time.sleep(31)

#     aut.moveTo(1415, 250) #shoikeepr
#     aut.click()
#     time.sleep(1)


#     aut.moveTo(1477, 330) #salj 1
#     aut.click()
#     time.sleep(1)


#     aut.moveTo(1818, 475) #salj alla
#     for i in range(28):
                
#         aut.click()
#         time.sleep(0.1)


# # while True:  
# #     for i in range(30):   
# #         aut.click()
# #         time.sleep(1)
# #         time.sleep(random.uniform(389, 577))
        

# while True:
#     aut.moveTo(1364, 55)
#     aut.click()
#     time.sleep(1)
#     aut.moveTo(1291, 153)
#     aut.click()
#     time.sleep(1)
#     aut.press("esc")
#     time.sleep(1)
#     for i in range(27):
#         aut.PAUSE = 0.05
#         aut.moveTo(1830, 477)
#         aut.click()
#         aut.moveTo(1787, 477)
#         aut.click()

#     time.sleep(1)

    





# while True:
#      aut.PAUSE = 0.1
    
#      aut.moveTo(1775, 290) # 
#      aut.click()



#      aut.moveTo(1775, 327) # 
#      aut.click()



    # PEDROVIC MITT NAMN



# for i in range(1):

#     aut.moveTo(1735, 260)
#     aut.click()

#     for i in range(6):
#         aut.moveRel(0 , +35 , duration=0.1)
#         aut.click()


#     aut.moveTo(1778, 260)
#     aut.click()

#     for i in range(6):
#         aut.moveRel(0 , +35 , duration=0.1)
#         aut.click()

    
#     aut.moveTo(1820, 260)
#     aut.click()

#     for i in range(6):
#         aut.moveRel(0 , +35 , duration=0.1)
#         aut.click()

#     aut.moveTo(1860, 260)
#     aut.click()

#     for i in range(6):
#         aut.moveRel(0 , +35 , duration=0.1)
#         aut.click()


# #cook huey platsen 417 kamera
# while True: 

#     aut.moveTo(1732,259) #food i invy
#     aut.click()
#     time.sleep(1)

#     aut.moveTo(1599,289) #oven
#     aut.click()
#     time.sleep(5)

#     aut.press("space")
#     time.sleep(67)

#     aut.moveTo(1270, 90)#bank
#     aut.click()
#     time.sleep(5)

#     aut.moveTo(1600, 340)#deposit
#     aut.click()
#     time.sleep(1)
#     aut.moveTo(1290, 164)#ta food
#     aut.click()
#     time.sleep(1)
#     aut.press("esc")

#herb
# while True: 
#         aut.moveTo(1531, 199)#shark
#         aut.click()
#         time.sleep(1)
#         aut.moveTo(1484, 199)#grapes
#         aut.click()
#         time.sleep(1)
#         aut.press("esc")
#         time.sleep(1)


#         aut.moveTo(1735, 367)# chisel
#         aut.click()
#         time.sleep(1)
#         aut.moveTo(1735, 406)#gems
#         aut.click()
#         time.sleep(1) 
#         aut.press("space")
#         time.sleep(18) 

#         aut.moveTo(1403, 161)# bank
#         aut.click()
#         time.sleep(1)
#         aut.moveTo(1597, 340)#deposit 
#         aut.click()
#         time.sleep(1)






 
def prif():
    aut.FAILSAFE = True

    # 1. BESTÄM OMRÅDET (x, y, bredd, höjd)
    # Här letar vi i en ruta som startar vid 0,0 och är 960x540 pixlar
    region_x, region_y, region_w, region_h =1150, 19, 1671, 361

    # 2. TA BILDEN ENBART DÄR
    screenshot = aut.screenshot(region=(region_x, region_y, region_w, region_h))
    frame = np.array(screenshot)

    # (Färgkonvertering och maskning - samma som innan)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])
    mask = cv.inRange(hsv, lower_pink, upper_pink)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(largest)

        # 3. JUSTERA MUSPOSITIONEN
        # Vi lägger till 'region_x' och 'region_y' så musen hittar rätt på hela skärmen
        mus_x = x + w // 2 + region_x
        mus_y = y + h // 2 + region_y

        print(f"Hittade Betty i zonen vid: {mus_x}, {mus_y}")
        aut.moveTo(mus_x, mus_y, duration=0.1)
        aut.click()
    else:
        print("Hittade inget i den valda zonen.")

# construction kamera 340
# while True:
#         time.sleep(1)

#         aut.moveTo(1482, 164)
#         aut.click()
#         time.sleep(1)
#         aut.press("esc")
#         time.sleep(1)
#         aut.press("4")
#         time.sleep(1)
#         aut.moveTo(1769, 317)#huset
#         aut.click()
#         time.sleep(4)
#         aut.press("2")

#         aut.moveTo(1243, 193)
#         aut.click()
#         time.sleep(4)


#         aut.press("4")
#         time.sleep(2)
#         aut.moveTo(1409, 220)
#         aut.click()
#         time.sleep(1)
#         aut.press("1")
#         time.sleep(1)

#         for i in range(5):
#             aut.moveTo(1409, 220)
#             aut.click()
#             time.sleep(1)
#             aut.press("4")
#             time.sleep(2)
#             aut.moveTo(1409, 220)
#             aut.click()
#             time.sleep(1)
#             aut.press("1")
#             time.sleep(1)

#         aut.moveTo(1731, 293)
#         aut.click()
#         time.sleep(4)

#         prif()
#         time.sleep(3)

# pray kamera 340
# while True:
#         time.sleep(1)

#         aut.moveTo(1530, 198)
#         aut.click()
#         time.sleep(1)
#         aut.press("esc")
#         time.sleep(1)
#         aut.press("4")
#         time.sleep(1)
#         aut.moveTo(1769, 317)#huset
#         aut.click()
#         time.sleep(4)
#         aut.press("2")

#         aut.moveTo(1798, 131)
#         aut.click()
#         time.sleep(4)

#         aut.moveTo(1415, 242)
#         aut.click()
#         time.sleep(2)


# for i in range(37):
#     aut.moveTo(1859, 475)
#     aut.click()

#     aut.moveTo(1414, 224)
#     aut.click()
            
            
        # aut.moveTo(1731, 293)
        # aut.click()
        # time.sleep(4)

        # prif()
        # time.sleep(3)



# nature runes kanmera 538 - 543 nu 
while True:
        
    

        aut.moveTo(1337, 162, duration=0.2)#essence
        aut.click()
        time.sleep(1)
        aut.press("esc")

        aut.moveTo(1733, 260, duration=0.2)# fill pouch 
        aut.click()
        time.sleep(1)
           

        aut.moveTo(1453, 204, duration=0.2)#   banker
        aut.click()
        time.sleep(1)

        aut.moveTo(1337, 162, duration=0.2)#essence
        aut.click()
        time.sleep(1)
        aut.press("esc")



        aut.moveTo(1826, 48)# gå
        aut.click()
        time.sleep(24)



        aut.moveTo(1807, 84)#innan shortcutten
        aut.click()
        time.sleep(7) 

        aut.moveTo(1375, 90)# shortcut
        aut.click()
        time.sleep(6)



        aut.moveTo(1795, 101) #mot altare
        aut.click()
        time.sleep(5)

        prif()
        time.sleep(3)

        prif()
        time.sleep(6)

        aut.moveTo(1733, 260, duration=0.2)# empty pouch 
        aut.click()
        time.sleep(1)

        prif()
        time.sleep(5)

        aut.moveTo(1410, 280) 
        aut.click()
        time.sleep(2)

        aut.moveTo(1415, 322) 
        aut.click()
        time.sleep(2)

        aut.moveTo(1807, 141) #mot shortcut
        aut.click()
        time.sleep(7)

        aut.moveTo(1455, 244) #shortcut
        aut.click()
        time.sleep(5)


        aut.moveTo(1782, 166) #mot ny shortcut 
        aut.click()
        time.sleep(11)

        prif()
        time.sleep(6)

        aut.moveTo(1775, 145) #mot bank
        aut.click()
        time.sleep(9)

        aut.moveTo(1458, 193) #banker 
        aut.click()
        time.sleep(2)

        aut.moveTo(1600, 340) #deposit 
        aut.click()
        time.sleep(2)


# for i in range (1):
#     aut.PAUSE = 0.05

#     aut.moveTo(1735, 257) 
#     aut.click()

#     for i in range(7):
#         aut.moveRel(0 , 30)
#         aut.click()


#     aut.moveTo(1779, 257) 
#     aut.click()
    
#     for i in range(7):
#         aut.moveRel(0 , 30)
#         aut.click()


#     aut.moveTo(1822, 257) 
#     aut.click()
    
#     for i in range(7):
#         aut.moveRel(0 , 30)
#         aut.click()


#     aut.moveTo(1862, 257) 
#     aut.click()
    
#     for i in range(7):
#         aut.moveRel(0 , 30)
#         aut.click()

# # #wrath -151 
# while True:
    
   

#     aut.moveTo(1360, 288) 
#     aut.click()
#     time.sleep(6)


#     aut.moveTo(1415, 168) 
#     aut.click()
#     time.sleep(6)

#     aut.moveTo(1790, 178) 
#     aut.click()
#     time.sleep(16)

#     aut.moveTo(1473, 285) 
#     aut.click()
#     time.sleep(6)


#     aut.moveTo(1423, 152) #altar
#     aut.click()
#     time.sleep(5)

#     aut.moveTo(1414, 162) #runes
#     aut.click()
#     time.sleep(6)

#     # aut.press("5")
#     # time.sleep(5)

#     # aut.moveTo(1755, 295) #teleport
#     # aut.click()
#     # time.sleep(6)

#     aut.moveTo(1414, 252) #portal
#     aut.click()
#     time.sleep(4)

#     aut.moveTo(1403, 226) #tunnel
#     aut.click()
#     time.sleep(6)

#     aut.moveTo(1409, 86) #stege
#     aut.click()
#     time.sleep(19)

#     aut.moveTo(1434, 322) # trappa
#     aut.click()
#     time.sleep(6)


#     aut.moveTo(1449, 156) # bank
#     aut.click()
#     time.sleep(6)

#     aut.moveTo(1600, 340) # deposit 
#     aut.click()
#     time.sleep(1)


#     aut.moveTo(1338, 162) # ta esssence
#     aut.click()
#     time.sleep(1)

#     aut.press("esc")
#     time.sleep(1)


