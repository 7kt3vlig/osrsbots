
import pyautogui as aut
import time 

#kamera 616 


def betty():
    aut.moveTo(2453, 378) 
    aut.click(button="right")
    aut.moveTo(2453, 458) 
    aut.click()
    time.sleep(1)
    aut.press("space")
    time.sleep(0.7)
    aut.press("2")
    time.sleep(0.7)
    aut.press("1")
    time.sleep(0.7)
    aut.press("space")
    time.sleep(0.7)
    aut.press("space")
    time.sleep(0.7) 
    aut.press("1")
    time.sleep(0.7)
    aut.press("space")


def fillcans():

    aut.moveTo(2453, 458)  
    time.sleep(1)
    aut.press("space")
    time.sleep(0.7)


#kamera -159 
def zentrees():
    aut.moveTo(2589, 364)  #trapporna
    time.sleep(1)
    aut.click()
    time.sleep(2)


    aut.moveTo(2168, 651)  #banken
    time.sleep(1)
    aut.click()
    time.sleep(11)

    aut.moveTo(2720, 147)  #tabben 
    aut.click()
    time.sleep(2)

    aut.moveTo(3378, 493)  #deposit kanna 
    aut.click()
    time.sleep(1)

    aut.moveTo(2872, 300)  #ta kanna 
    aut.click()
    time.sleep(1)

    aut.moveTo(2505, 305)  #ta dye
    aut.click()
    time.sleep(0.6)
    aut.click()
    time.sleep(0.6)
    aut.click()
    time.sleep(0.6)

    aut.moveTo(2625, 305)  #ta plants
    aut.click()
    time.sleep(0.6)
    aut.click()
    time.sleep(0.6)
    aut.click()
    time.sleep(0.6)

    aut.moveTo(2745, 305)  #ta sand 
    aut.click()
    time.sleep(1)

    aut.press("esc")
    time.sleep(1)

    aut.moveTo(3480, 485)  #tp house
    aut.click()
    time.sleep(6)

    aut.moveTo(2624, 345)  #gå till trädet
    aut.click()
    time.sleep(3)

    for i in range (3):
        aut.moveTo(2563, 347)  #högerklicka trädet
        aut.click(button="right")
        time.sleep(0.7)
        aut.moveTo(2563, 457)  #build
        aut.click()
        time.sleep(1)
        aut.press("1")
        time.sleep(1.2)


        aut.moveTo(2563, 347)  #högerklicka zen
        aut.click(button="right")
        time.sleep(0.7)
        aut.moveTo(2563, 457)  #remove
        aut.click()
        time.sleep(0.7)
        aut.press("1")
        time.sleep(1.2)

    
    aut.moveTo(3680, 480)  #seedpod
    aut.click()
    time.sleep(6)


# -159 
while True:
        
    zentrees()

# for i in range (27):
    
#     betty()

 