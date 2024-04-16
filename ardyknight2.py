import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
import random 

def ardyknight():
    print("Stealing..")
    aut.moveTo(63, 217)
    aut.click()
    time.sleep(0.6)

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
    else:
        print("No match found, continuing with the script ")

def detect_hp():
    print("checking hp..")
    # Define the region of interest (ROI) coordinates
    roi_top_left = (525, 83)
    roi_bottom_right = (543, 95)
    
    screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                        roi_bottom_right[0] - roi_top_left[0], 
                                        roi_bottom_right[1] - roi_top_left[1]))

    # Convert the screenshot to OpenCV format (BGR)
    screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    # Load the template image
    template = cv.imread('hp.png', cv.IMREAD_GRAYSCALE)
    blur = cv.blur(grayscale_img, (3,3))
    blur1 = cv.blur(template, (3,3))
    canny = cv.Canny(blur, 125, 175)
    canny1 = cv.Canny(blur1, 125, 175)

    # Perform template matching
    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

    # Define a threshold for the match
    threshold = 0.4

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
        aut.click(x_center, y_center)
        print("Clicked at:", (x_center, y_center))
        time.sleep(0.6)
        aut.keyDown("shift")
        aut.click()
        aut.keyUp("shift")
    else:
        print("No matches found.")

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

# Define the region coordinates
x1, y1 = 8, 31
x2, y2 = 520, 366

# Take a screenshot of the specified region
screenshot = aut.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

# Convert the screenshot to OpenCV format (BGR)
screenshot_cv = np.array(screenshot)

# Convert BGR to HSV
hsv = cv.cvtColor(screenshot_cv, cv.COLOR_RGB2HSV)

# Define lower and upper bounds for yellow color
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

# Threshold the HSV image to get only yellow colors
mask = cv.inRange(hsv, lower_yellow, upper_yellow)

# Apply Canny edge detection
edges = cv.Canny(mask, 30, 150)

# Find contours in the edge-detected image
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw contours on the screenshot image
screenshot_with_contours = screenshot_cv.copy()
cv.drawContours(screenshot_with_contours, contours, -1, (0, 255, 0), 2)

# Display the screenshot image with the contours
cv.imshow('Screenshot with Contours', screenshot_with_contours)
cv.waitKey(0)
cv.destroyAllWindows()
# print("Restocking and detecting..")

# Restock
# print("Restocking..")


# aut.moveTo(680, 210)
# aut.click()
# time.sleep(0.2)
# aut.moveTo(605, 300)
# aut.click()
# time.sleep(4)
# aut.moveTo(260, 240)
# aut.scroll(-5000)   # scroll up 10 "clicks"



# aut.moveTo(172, 273)
# aut.click()
# time.sleep(4)


# aut.moveTo(140, 127)
# aut.click()
# time.sleep(0.6)

# aut.moveTo(583, 260)
# aut.click()

# aut.moveTo(626, 260)
# aut.click()

# aut.press("esc")


# aut.moveTo(750, 215)
# aut.click()
# time.sleep(0.2)
# aut.moveTo(647, 341)
# aut.click()
# time.sleep(4)


# aut.moveTo(650, 215) #tp till ardy 
# aut.click()


# print("Detecting the item..")
# template = cv.imread('bankikon.png', cv.IMREAD_GRAYSCALE)
# template_height, template_width = template.shape

# roi_top_left = (577, 77)
# roi_bottom_right = (612, 120)
# screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
#                                     roi_bottom_right[0] - roi_top_left[0], 
#                                     roi_bottom_right[1] - roi_top_left[1]))

# screenshot_np = np.array(screenshot)

# # Apply Gaussian blur to the screenshot
# screenshot_blurred = cv.GaussianBlur(screenshot_np, (7, 7), 0)

# # Convert the blurred screenshot to grayscale
# screenshot_gray = cv.cvtColor(screenshot_blurred, cv.COLOR_RGB2GRAY)

# # Apply Gaussian blur to the template
# template_blurred = cv.GaussianBlur(template, (7, 7), 0)

# # Convert the blurred template to grayscale
# template_gray = cv.cvtColor(template_blurred, cv.COLOR_GRAY2BGR)

# # Convert both the screenshot and template to Canny edges
# screenshot_edges = cv.Canny(screenshot_gray, 125, 175)
# template_edges = cv.Canny(template_gray, 125, 175)
# cv.imshow("1", screenshot_edges)
# cv.imshow("2", template_edges )
# cv.waitKey(0)
# cv.destroyAllWindows()
# # Perform template matching
# result = cv.matchTemplate(screenshot_edges, template_edges, cv.TM_CCOEFF_NORMED)

# # Find the location of the maximum value
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# # Convert the max_loc to the actual screen location
# max_loc_screen = (max_loc[0] + roi_top_left[0], max_loc[1] + roi_top_left[1])

# # Print the maximum value and its screen location
# print("Max value:", max_val)
# print("Max location (on screen):", max_loc_screen)

# # Move the mouse to the center of the detected item and click
# item_center_x = max_loc_screen[0] + template_width // 2
# item_center_y = max_loc_screen[1] + template_height // 2
# aut.moveTo(item_center_x, item_center_y)
# aut.click()


# while True:
#     detect_coin_pouches()
#     detect_hp()
#     ardyknight()







