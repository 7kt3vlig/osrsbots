import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os 

def taenergy():
    aut.moveTo(936, 89) #energy tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(664, 118) #ta pot 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(1154, 254) #drick 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.8)

    aut.moveTo(827, 192) #bankern 
    time.sleep(0.4)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.4)

def taenergy2():
    aut.moveTo(936, 89) #energy tabben
    time.sleep(0.5)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(664, 118) #ta pot 
    aut.click()
    time.sleep(0.4)
    aut.press("esc")

    aut.moveTo(1154, 254) #drick 
    time.sleep(0.4)
    aut.click()
    time.sleep(0.8)
    aut.click()


    aut.moveTo(827, 192) #bankern 
    time.sleep(0.4)
    aut.click()
    time.sleep(1)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(0.4)




def dit2():
    aut.moveTo(1283, 130) #vid banken 1a steget 
    time.sleep(1)
    aut.click()
    time.sleep(20)

    aut.moveTo(1218, 182) #2
    time.sleep(1)
    aut.click()
    time.sleep(25)

    aut.moveTo(654, 283) #3 klämm igenom grejjen 
    time.sleep(1)
    aut.click()
    time.sleep(14)

    aut.moveTo(1229, 143) #4
    time.sleep(1)
    aut.click()
    time.sleep(16)

    aut.moveTo(889, 323) #5 på rune altar grejjen 
    time.sleep(1)
    aut.click()
    time.sleep(5)

def dit(): 

    aut.moveTo(1283, 130) #vid banken 1a steget 
    aut.click()
    time.sleep(10)

    aut.moveTo(1218, 182) #2
    time.sleep(1)
    aut.click()
    time.sleep(13)

    aut.moveTo(654, 283) #3 klämm igenom grejjen 
    time.sleep(0.2)
    aut.click()
    time.sleep(10)

    aut.moveTo(1229, 143) #4
    time.sleep(1)
    aut.click()
    time.sleep(8)

    aut.moveTo(889, 323) #5 på rune altar grejjen 
    time.sleep(1)
    aut.click()
    time.sleep(4)

def tbx2():
    aut.moveTo(1203, 69) #1
    time.sleep(1)
    aut.click()
    time.sleep(18)

    aut.moveTo(875, 169) #busken 2 
    aut.click()
    time.sleep(7)

    aut.moveTo(1236, 52) #3 
    aut.click()
    time.sleep(28)

    aut.moveTo(1173, 52) #4
    aut.click()
    time.sleep(25)

    aut.moveTo(739, 232) #banken
    aut.click()
    time.sleep(5)

def tbx():

    aut.moveTo(1203, 69) #1
    time.sleep(1)
    aut.click()
    time.sleep(10)
    aut.moveTo(875, 169) #busken 2 
    aut.click()
    time.sleep(6)

    aut.moveTo(1236, 52) #3 
    aut.click()
    time.sleep(15)

    aut.moveTo(1173, 52) #4
    aut.click()
    time.sleep(13)

    aut.moveTo(740, 232) #banken
    aut.click()
    time.sleep(3)

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(0.4)

def banka():
    aut.moveTo(895, 83) #rune tabben 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(809, 118) #ta pouch  3
    aut.click()
    time.sleep(0.2)

    aut.moveTo(761, 118) #ta pouch 2
    aut.click()
    time.sleep(0.2)

    aut.moveTo(713, 118) #ta pouch 1
    aut.click()
    time.sleep(0.2)

    
    

    aut.moveTo(664, 118) #ta essence 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(1154, 254) #fyll pouchen 
    
    aut.click()
    time.sleep(0.4)

    aut.moveTo(1197, 254) #fyll pouch 2
    
    aut.click()
    time.sleep(0.4)

    aut.moveTo(1239, 254) #fyll pouch  3
    aut.click()
    time.sleep(0.4)

    aut.moveTo(827, 192) #bankern 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(664, 118) #ta essence 
    aut.click()
    time.sleep(0.2)
    aut.press("esc")
    
def banka2():

    aut.moveTo(1021, 335) #banka allt 
    time.sleep(0.5)
    aut.click()
    time.sleep(1)

    aut.moveTo(664, 118) #ta essence 
    aut.click()
    time.sleep(0.4)
    aut.press("esc")




    

def kollaspring(): 
    try:
        screenshot = ImageGrab.grab(bbox=(1106, 143, 1129, 158))#847, 214, 861, 228)
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        
        # Load the template image
        template = cv.imread("100run.png")
        
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
            aut.moveTo(1144, 146)
            time.sleep(1)
            aut.click()
        else:
            pass


def kollaostra():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("ostra.png")
        
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
            aut.moveTo(583, 189) #östra 
            time.sleep(1)
            aut.click()
            time.sleep(6)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1239, 254) #pouch  3
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(1)

            aut.moveTo(809, 191)
            aut.click()
            time.sleep(1)

            aut.moveTo(1083, 195) #tbx 
            time.sleep(1)
            aut.click()
            time.sleep(5)
        else:
            pass

def kollavastra():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("vastra.png")
        
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
            aut.moveTo(1089, 185) #västra 
            time.sleep(1)
            aut.click()
            time.sleep(6)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1239, 254) #pouch  3
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(1)

            aut.moveTo(864, 194)
            aut.click()


            aut.moveTo(590, 193) #tbx
            time.sleep(1)
            aut.click()
            time.sleep(5)
            
        else:
            pass

def kollasodra():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("sodra.png")
        
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
            aut.moveTo(837, 34) #södra 
            time.sleep(1)
            aut.click()
            time.sleep(6)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1239, 254) #pouch  3
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(1)

            aut.moveTo(835, 168)
            aut.click()



            aut.moveTo(1219, 143) #tbx
            time.sleep(1)
            aut.click()
            time.sleep(7)
            aut.moveTo(837, 205)
            aut.click()
            
        else:
            pass

def kollanorra():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("norra.png")
        
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
            aut.moveTo(1219, 143) #norra 
            time.sleep(1)
            aut.click()
            time.sleep(7)
            aut.moveTo(836, 231)
            time.sleep(1)
            aut.click()
            time.sleep(2)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1239, 254) #pouch  3
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(1)

            aut.moveTo(836, 231)
            aut.click()

            aut.moveTo(837, 45) #tbx
            time.sleep(1)
            aut.click()
            time.sleep(5)

        else:
            pass


def kollaostra2():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("ostra.png")
        
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
            aut.moveTo(583, 189) #östra 
            time.sleep(1)
            aut.click()
            time.sleep(13)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(0.5)

            aut.moveTo(809, 191)
            aut.click()
            time.sleep(1)

            aut.moveTo(1083, 195) #tbx 
            time.sleep(1)
            aut.click()
            time.sleep(12)
        else:
            pass

def kollavastra2():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("vastra.png")
        
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
            aut.moveTo(1089, 185) #västra 
            time.sleep(1)
            aut.click()
            time.sleep(13)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(0.5)

            aut.moveTo(864, 194)
            aut.click()


            aut.moveTo(590, 193) #tbx
            time.sleep(1)
            aut.click()
            time.sleep(12)
            
        else:
            pass

def kollasodra2():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("sodra.png")
        
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
            aut.moveTo(837, 34) #södra 
            time.sleep(1)
            aut.click()
            time.sleep(13)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254) #pouch 2
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(0.5)

            aut.moveTo(835, 168)
            aut.click()



            aut.moveTo(1219, 143) #tbx
            time.sleep(1)
            aut.click()
            time.sleep(14)
            aut.moveTo(837, 205)
            aut.click()
            time.sleep(1)
        else:
            pass

def kollanorra2():
    try:
        screenshot = ImageGrab.grab(bbox=(1163, 36, 1250, 143))
        screenshot.save("sample.png")
        screenshot.close()
        screenshot = np.array(Image.open("sample.png"))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        
        # Load the template image
        template = cv.imread("norra.png")
        
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
            aut.moveTo(1219, 143) #norra 
            time.sleep(1)
            aut.click()
            time.sleep(13)
            aut.moveTo(836, 231)
            time.sleep(1)
            aut.click()
            time.sleep(2)
            aut.keyDown("shift")
            aut.moveTo(1155, 254) #pouch 1 
            time.sleep(0.5)
            aut.click()
            aut.moveTo(1197, 254)#pouch 2
            time.sleep(0.5)
            aut.click()
            aut.keyUp("shift")
            time.sleep(0.5)

            aut.moveTo(836, 231)
            aut.click()

            aut.moveTo(837, 45) #tbx
            time.sleep(1)
            aut.click()
            time.sleep(12)

        else:
            pass



#aut.moveTo(1089, 185)  västra  
#aut.moveTo(583, 189)  östtraa
#aut.moveTo(837, 34)  södra 
#aut.moveTo(1219, 143 o sen 836 231 )  norra 
    
def snabb():

    dit()
    kollanorra()
    kollaostra()
    kollasodra()
    kollavastra()
    tbx()
    

while True:
    snabb()
    taenergy()
    banka()
    


    

#nästa -> gör en timer med threading i en miniversion först dock 
    
