import pyautogui as aut
import time 


def firemake():

    #rad 1 
    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,762)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,762)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,762)
    aut.click()
    time.sleep(2.4)

    #rad 2 
    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(585,800)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,800)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,800)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,800)
    aut.click()
    time.sleep(2.4)

    
    #rad 3
    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(585,836)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,836)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,836)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,836)
    aut.click()
    time.sleep(2.4)

    #rad 4

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(585,871)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,871)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,871)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,871)
    aut.click()
    time.sleep(2.4)

    #rad 5 

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(585,908)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,908)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,908)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,908)
    aut.click()
    time.sleep(2.4)

    #rad 6 

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(585,946)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,946)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,946)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,946)
    aut.click()
    time.sleep(2.4)

    #rad 7 

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(585,979)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(625,979)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(668,979)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(585,762)
    aut.click()
    aut.moveTo(710,979)
    aut.click()
    time.sleep(2.4)

    aut.moveTo(695, 593) #gå till banken  
    aut.click()
    time.sleep(7)


def banka():
    


    aut.moveTo(367, 704)  #banker
    time.sleep(0.2)
    aut.click()
    time.sleep(0.5)

    aut.moveTo(122, 596)  #fletch tabben
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(449, 846) #banka allt 
    time.sleep(0.2)
    aut.click()
    time.sleep(0.2)

    aut.moveTo(192, 633) #ta knife 
    aut.click()
    time.sleep(0.2)

    aut.moveTo(140, 632) #ta logs  
    aut.click()
    time.sleep(0.2)
    aut.press("esc")

    aut.moveTo(707, 640) #gå till platsen 
    aut.click()
    time.sleep(7)

    




while True():

    banka()
    firemake()

