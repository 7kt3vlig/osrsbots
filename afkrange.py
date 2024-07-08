import pyautogui as aut
import time 

def taochdroppa():
    aut.moveTo(329, 396)
    aut.click()
    time.sleep(1)
    aut.keyDown("shift")
    aut.moveTo(700, 500)
    aut.click()
    aut.keyUp("shift")
    time.sleep(3)

def alchorange():
    
    for i in range(10):
        aut.moveTo(1532, 642)
        aut.click()
        
        time.sleep(0.5)

    aut.moveTo(558, 382)
    aut.click()
    aut.click()
    time.sleep(3)
    
def range():

    aut.moveTo(558, 382)
    aut.click()
    time.sleep(20)


while True:
    range()
    
# while True:
    
#     # taochdroppa()
        
#     for i in range (700):
#         # aut.moveTo(2479, 377)
#         # aut.click()
#         # time.sleep(30)

#         aut.moveTo(558, 382)
#         aut.click()
#         time.sleep(30)

#     aut.moveTo(2479, 377)
#     aut.click(button="right")
#     aut.moveTo(2479, 462)
#     aut.click()
#     time.sleep(30)

# def plockaupp():
        
#     aut.moveTo(559, 374)
#     aut.click(button="right")
#     aut.moveTo(559, 462)
#     aut.click()
#     time.sleep(30)



# for i in range(2650):
#     alchorange()
# plockaupp()