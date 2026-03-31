import pyautogui as aut
import numpy as np
import cv2 as cv
import time

# Load the template image
leaf_template = cv.imread("leaf.png")

aut.PAUSE = 0

# Store all results of matches
match_results = []

# Best match tracking variables
best_match = {
    "value": 0,          # The best match value (max_val)
    "location": (0, 0),  # The location of the best match (max_loc)
    "timestamp": 0       # The timestamp when the best match was found
}

def leaf():
    top_left = (1200, 341)
    bottom_right = (1681, 817)
    
    # Debug print to check the region coordinates
    print(f"Top left: {top_left}, Bottom right: {bottom_right}")
    
    # Load the template image and convert to grayscale
    template = cv.imread("leaf.png")
    
    if template is None:
        print("Template image leaf.png not found or unable to load.")
        return False

    # Convert the template to grayscale
    template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    template_eq = cv.equalizeHist(template_gray)

    # Define the threshold for a match
    threshold = 0.52

    # Capture the screenshot of the specified region using pyautogui
    try:
        screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                            bottom_right[0] - top_left[0],
                                            bottom_right[1] - top_left[1]))
        screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error capturing screenshot with pyautogui: {e}")
        return False

    # Convert the screenshot to grayscale
    screenshot_gray = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Apply histogram equalization to the screenshot to improve contrast
    screenshot_eq = cv.equalizeHist(screenshot_gray)

    # Perform template matching using the equalized grayscale images
    result = cv.matchTemplate(screenshot_eq, template_eq, cv.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("Printing matching values:")
    print(f"Min value: {min_val}, Max value: {max_val}, Min location: {min_loc}, Max location: {max_loc}")

    # Store the current match in the list
    match_results.append({
        "value": max_val,
        "location": max_loc,
        "timestamp": time.time()  # Store the timestamp when the match occurred
    })

    # If the match is above the threshold, check if it's the best match so far
    if max_val >= threshold:
        print("Match found. Clicking on the position.")
        aut.click()

        # Check if the current match is the best match so far
        if max_val > best_match["value"]:
            best_match["value"] = max_val
            best_match["location"] = max_loc
            best_match["timestamp"] = time.time()
            print(f"New best match found at {best_match['location']} with value {best_match['value']}.")

        return True
    else:
        print("No match found above the threshold.")
        return False

def print_best_match():
    if best_match["value"] > 0:
        print(f"Best match during this session: Location = {best_match['location']}, Value = {best_match['value']}")
    else:
        print("No match found during this session.")

while True:
    leaf()
    # Optionally print the best match periodically, for example every 10 seconds
    # time.sleep(5)
    # print_best_match()