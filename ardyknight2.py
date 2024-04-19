import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 



def refilldodgyneck():
    print("checking dodgyneck..")

    aut.moveTo(680, 215)#gear tab
    time.sleep(0.2)
    aut.click()

# Define the region of interest (ROI) coordinates
    roi_top_left = (627, 275)
    roi_bottom_right = (664, 310)

    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                        roi_bottom_right[0] - roi_top_left[0], 
                                        roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


    # Convert the filtered image to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('dodgyneck.png', cv.IMREAD_GRAYSCALE)

    # Blur both the grayscale image and the template
    blur = cv.blur(grayscale_img, (3,3))
    blur1 = cv.blur(template, (3,3))

    # Apply Canny edge detection to both images
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)

    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

        # Define a threshold for the match
    threshold = 0.53

    # Get the location of the best match
    _, max_val, _, _ = cv.minMaxLoc(result)

    # Check if the maximum match value is above the threshold
    if max_val >= threshold:
        print("Match found! not going to get necklace")
        print("Max value:", max_val)
        aut.moveTo(650,215)#tillbaka till inventory tabben
        time.sleep(0.2)
        aut.click()
    else:
        print("No match found, going to get a new necklace..")
        print("Max value:", max_val)
        time.sleep(5.5)
        aut.moveTo(650,215)#tillbaka till inventory tabben
        time.sleep(0.2)
        aut.click()
        aut.moveTo(582, 260)#töm pouches 
        time.sleep(1)
        aut.click()
        aut.click()
        aut.moveTo(490,292)#gå framför banken 
        time.sleep(0.2)
        aut.click()
        time.sleep(3)
        aut.moveTo(342, 292)#bank
        aut.click()
        time.sleep(1)
        aut.moveTo(239, 126)#neck
        aut.click()
        time.sleep(0.6)
        aut.press("esc")

        aut.moveTo(582, 260)#wear necklace 
        time.sleep(0.2)
        aut.click()
        time.sleep(2)

        aut.moveTo(73, 177)#tillbaka / ardy knight i banken
        aut.click()
        time.sleep(4)
        
        



def ardyknight():
    print("Stealing..")
    aut.moveTo(267, 135)
    aut.click()
    time.sleep(0.3)

def detect_coin_pouches():
    
    print("checking pouches..")
    # Define the region of interest (ROI) coordinates
    roi_top_left = (560, 235)
    roi_bottom_right = (597, 272)

    # Take a screenshot of the specified region
    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                         roi_bottom_right[0] - roi_top_left[0], 
                                         roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('coinpouches.png', cv.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv.matchTemplate(grayscale_img, template, cv.TM_CCOEFF_NORMED)

    # Define a threshold for the match
    threshold = 0.9

    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Check if the maximum match value is above the threshold
    if max_val >= threshold:
        print("detected pouches, clicking them")
        aut.moveTo(582, 260)
        time.sleep(0.2)
        aut.click()
        # Reset the timer by returning the current time
        return True
    else:
        print("No match found, continuing with the script ")
        return False

def detect_hp():
    print("checking hp..")
# Define the region of interest (ROI) coordinates
    roi_top_left = (526, 72)
    roi_bottom_right = (572, 95)

    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                        roi_bottom_right[0] - roi_top_left[0], 
                                        roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


    # Convert the filtered image to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('hp.png', cv.IMREAD_GRAYSCALE)

    # Blur both the grayscale image and the template
    blur = cv.blur(grayscale_img, (3,3))
    blur1 = cv.blur(template, (3,3))

    # Apply Canny edge detection to both images
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)

    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

        # Define a threshold for the match
    threshold = 0.49

    # Get the location of the best match
    _, max_val, _, _ = cv.minMaxLoc(result)

    # Check if the maximum match value is above the threshold
    if max_val >= threshold:
        print("Match found! not going to eat")
        print("Max value:", max_val)
    else:
        print("No match found, going to eat..")
        print("Max value:", max_val)
        print("detecting jugs in inventory..")
        
        # Perform jug detection and click on one if found
        detect_jugs_and_drink()

def detect_jugs_and_drink():
    roi_top_left = (553, 310)
    roi_bottom_right = (737, 489)

    # Take a screenshot of the region where jugs are expected to be
    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                         roi_bottom_right[0] - roi_top_left[0], 
                                         roi_bottom_right[1] - roi_top_left[1]))

    screenshot_cv1 = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2GRAY)
    template1 = cv.imread('jugofwine.png', cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(screenshot_cv1, template1, cv.TM_CCOEFF_NORMED)

    threshold = 0.40

    locations = np.where(result >= threshold)

    # Adjust the match locations to the actual screen coordinates
    match_locations = zip(*locations[::-1])
    adjusted_locations = [(pt[0] + roi_top_left[0], pt[1] + roi_top_left[1]) for pt in match_locations]

    # Prepare bounding boxes for non-maximum suppression
    boxes = []
    for pt in adjusted_locations:
        x, y = pt
        w, h = template1.shape[::-1]  # Width and height of the template
        boxes.append((x, y, w, h))

    # Apply non-maximum suppression to remove redundant detections
    picked_boxes = non_max_suppression(boxes, overlap_threshold=0.5)

    # Print the adjusted locations and corresponding match values
    for box in picked_boxes:
        x, y, _, _ = box
        print("Match found at:", (x, y))
        print("Match value:", result[y - roi_top_left[1], x - roi_top_left[0]])

    # Randomly select one of the remaining bounding boxes and click on its center
    if picked_boxes:
        # Randomly select a bounding box
        selected_box = random.choice(picked_boxes)
        # Get the center coordinates of the bounding box
        x_center = selected_box[0] + selected_box[2] // 2
        y_center = selected_box[1] + selected_box[3] // 2
        # Click on the center coordinates
        time.sleep(0.6)
        aut.click(x_center, y_center)
        aut.click(x_center, y_center)
        print("Clicked at:", (x_center, y_center))
        time.sleep(1)
        aut.keyDown("shift")
        time.sleep(1)
        aut.click()
        aut.keyUp("shift")
    else:
        print("No matches found.")
        banka()

def non_max_suppression(boxes, overlap_threshold):
    if len(boxes) == 0:
        return []

    # Sort the bounding boxes by their confidence score (match value)
    boxes = sorted(boxes, key=lambda x: x[2], reverse=True)

    # Initialize the list of picked bounding boxes
    picked_boxes = []

    # Loop over the sorted bounding boxes
    while len(boxes) > 0:
        # Get the bounding box with the highest confidence score
        best_box = boxes.pop(0)
        picked_boxes.append(best_box)

        # Calculate the intersection over union (IoU) with the other bounding boxes
        for box in boxes[:]:
            x1 = max(best_box[0], box[0])
            y1 = max(best_box[1], box[1])
            x2 = min(best_box[0] + best_box[2], box[0] + box[2])
            y2 = min(best_box[1] + best_box[3], box[1] + box[3])

            intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)
            area1 = best_box[2] * best_box[3]
            area2 = box[2] * box[3]
            iou = intersection_area / float(area1 + area2 - intersection_area)

            # Remove the bounding box if the IoU is greater than the overlap threshold
            if iou > overlap_threshold:
                boxes.remove(box)

    return picked_boxes

# # Define the region coordinates
# x1, y1 = 8, 31
# x2, y2 = 520, 366

# # Take a screenshot of the specified region
# screenshot = aut.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

# # Convert the screenshot to OpenCV format (BGR)
# screenshot_cv = np.array(screenshot)

# # Convert BGR to HSV
# hsv = cv.cvtColor(screenshot_cv, cv.COLOR_RGB2HSV)

# # Define lower and upper bounds for yellow color
# lower_yellow = np.array([20, 100, 100])
# upper_yellow = np.array([40, 255, 255])

# # Threshold the HSV image to get only yellow colors
# mask = cv.inRange(hsv, lower_yellow, upper_yellow)

# # Apply Canny edge detection
# edges = cv.Canny(mask, 30, 150)

# # Find contours in the edge-detected image
# contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# # Draw contours on the screenshot image
# screenshot_with_contours = screenshot_cv.copy()
# cv.drawContours(screenshot_with_contours, contours, -1, (0, 255, 0), 2)

# # Display the screenshot image with the contours
# cv.imshow('Screenshot with Contours', screenshot_with_contours)
# cv.waitKey(0)
# cv.destroyAllWindows()
# print("Restocking and detecting..")

def banka():
    time.sleep(5.5)
    aut.moveTo(505,290)#gå framför banken 
    time.sleep(0.6)
    aut.click()
    time.sleep(3)
    aut.moveTo(342, 292)#bank
    time.sleep(0.2)
    aut.click()
    time.sleep(1)

    aut.moveTo(198, 131)#jugs 
    aut.click()
    time.sleep(1)

    aut.moveTo(582, 260)#
    aut.click()
    time.sleep(0.6)
    aut.moveTo(582, 296)#
    aut.click()
    time.sleep(0.6)
    aut.moveTo(624, 296)#
    aut.click()
    time.sleep(0.6)
    aut.press("esc")

    aut.moveTo(73, 177)#tillbaka / ardy knight i banken
    aut.click()
    time.sleep(4)


#ta hänsyn till stun vid varje grej man gör 


def check_timer(start_time):
    elapsed_time = time.time() - start_time
    if elapsed_time >= 120:  # 2 minutes = 180 seconds
        print("No coin pouches found after 5 minutes. Exiting the script.")
        exit()
    else:
        return time.time()  # Return current time to reset the timer

# Main loop
while True:
    start_time = time.time()  # Start the timer
    for i in range(80):
        if detect_coin_pouches():
            start_time = time.time()  # Reset the timer if coin pouches were detected
        detect_hp()
        ardyknight()
        start_time = check_timer(start_time)  # Check if 2 minutes have passed and reset the timer if needed
    refilldodgyneck()
    







