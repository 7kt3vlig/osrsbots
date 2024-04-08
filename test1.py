import cv2 as cv 
import numpy as np
from PIL import ImageGrab, Image
from matplotlib import pyplot as plt
import pyautogui as aut


screenshot = ImageGrab.grab(bbox=(11,541,560,890))
screenshot.save("testis.png")
img = cv.imread("testis.png")


finna = aut.locateCenterOnScreen("reset.png", confidence=0.5)


