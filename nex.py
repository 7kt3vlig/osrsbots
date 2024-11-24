import pyautogui as aut
import numpy as np
import cv2 as cv
from pynput.keyboard import Key, Listener
import math
import time 








# 1. scanna hp baren - om den är mindre än 2720, 2040, 1360,680 så tryck på marken?
# 2. ät brew, scanna din hp bar 
# 3. drick restore och scanna prayer bar 
# 4. 

# drick brew 


brew1 = cv.imread("brew(1).png")
brew2 = cv.imread("brew(2).png")
brew3 = cv.imread("brew(3).png")
brew4 = cv.imread("brew(4).png")


restore1 = cv.imread("restore(1).png")
restore2 = cv.imread("restore(2).png")
restore3 = cv.imread("restore(3).png")
restore4 = cv.imread("restore(4).png")


stam1 = cv.imread("stam(1).png")
stam2 = cv.imread("stam(2).png")
stam3 = cv.imread("stam(3).png")
stam4 = cv.imread("stam(4).png")


def drickbrew():
    # List of template images in priority order
    template_files = ["brew(1).png", "brew(2).png", "brew(3).png", "brew(4).png"]
    
    # Debug print
    print("Capturing the entire screen for drickbrew matching.")
    
    # Capture the entire screen using pyautogui
    try:
        screenshot = aut.screenshot()  # Capture the entire screen
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Define the threshold for a match
    threshold = 0.8

    # Iterate through each template image in priority order
    for template_file in template_files:
        # Load the template image
        template = cv.imread(template_file)
        if template is None:
            print(f"Template image {template_file} not found or unable to load.")
            continue

        # Perform template matching
        result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
        
        # Get the best match position
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(f"Matching values for {template_file}:")
        print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
        
        # If the match is above the threshold, click on it
        if max_val >= threshold:
            print(f"Match found for {template_file}.")

            # Calculate the center of the match
            match_center = (
                max_loc[0] + template.shape[1] // 2,  # x-coordinate of the center
                max_loc[1] + template.shape[0] // 2   # y-coordinate of the center
            )

            # Perform a click at the match center
            aut.click(match_center[0], match_center[1])
            print(f"Clicked at: {match_center}")

            return True  # Stop after the first match in priority order

    print("No match found above the threshold for any template.")
    return False


def drickrestore():
    # List of template images in priority order
    template_files = ["restore(1).png", "restore(2).png", "restore(3).png", "restore(4).png"]
    
    # Debug print
    print("Capturing the entire screen for drickrestore matching.")
    
    # Capture the entire screen using pyautogui
    try:
        screenshot = aut.screenshot()  # Capture the entire screen
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Define the threshold for a match
    threshold = 0.8

    # Iterate through each template image in priority order
    for template_file in template_files:
        # Load the template image
        template = cv.imread(template_file)
        if template is None:
            print(f"Template image {template_file} not found or unable to load.")
            continue

        # Perform template matching
        result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
        
        # Get the best match position
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(f"Matching values for {template_file}:")
        print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
        
        # If the match is above the threshold, click on it
        if max_val >= threshold:
            print(f"Match found for {template_file}.")

            # Calculate the center of the match
            match_center = (
                max_loc[0] + template.shape[1] // 2,  # x-coordinate of the center
                max_loc[1] + template.shape[0] // 2   # y-coordinate of the center
            )

            # Perform a click at the match center
            aut.click(match_center[0], match_center[1])
            print(f"Clicked at: {match_center}")

            return True  # Stop after the first match in priority order

    print("No match found above the threshold for any template.")
    return False


def drickstam():
    # List of template images in priority order
    template_files = ["stam(1).png", "stam(2).png", "stam(3).png", "stam(4).png"]
    
    # Debug print
    print("Capturing the entire screen for drickstam matching.")
    
    # Capture the entire screen using pyautogui
    try:
        screenshot = aut.screenshot()  # Capture the entire screen
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Define the threshold for a match
    threshold = 0.8

    # Iterate through each template image in priority order
    for template_file in template_files:
        # Load the template image
        template = cv.imread(template_file)
        if template is None:
            print(f"Template image {template_file} not found or unable to load.")
            continue

        # Perform template matching
        result = cv.matchTemplate(screenshot_cv, template, cv.TM_CCOEFF_NORMED)
        
        # Get the best match position
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(f"Matching values for {template_file}:")
        print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")
        
        # If the match is above the threshold, click on it
        if max_val >= threshold:
            print(f"Match found for {template_file}.")

            # Calculate the center of the match
            match_center = (
                max_loc[0] + template.shape[1] // 2,  # x-coordinate of the center
                max_loc[1] + template.shape[0] // 2   # y-coordinate of the center
            )

            # Perform a click at the match center
            aut.click(match_center[0], match_center[1])
            print(f"Clicked at: {match_center}")

            return True  # Stop after the first match in priority order

    print("No match found above the threshold for any template.")
    return False


def scanhp():
    top_left = (1026, 660)
    bottom_right = (1069, 702)

def scanpray():
    top_left = (1026, 660)
    bottom_right = (1069, 702)


def scanrun():
    top_left = (1026, 660)
    bottom_right = (1069, 702)

def kollaomrundanstartar():


def attackeranex():

def attackeraintenex():

def attackerafumus():

def attackeraumbra():

def attackeracruor():

def attackeraglacies():




def main():
    





if __name__ == "__main__":
    main()