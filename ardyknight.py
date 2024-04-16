import pyautogui as aut
import numpy as np 
import cv2 as cv 
import time 
from PIL import ImageGrab, Image 
import os
import pytesseract
from PIL import Image


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

    # cv.imshow("1", canny)
    # cv.imshow("2", canny1)
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
        aut.moveTo(582, 333)  
        time.sleep(0.2)
        aut.click()
        
        
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

roi_top_left = (553, 377)
roi_bottom_right = (737, 489)

screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
                                     roi_bottom_right[0] - roi_top_left[0], 
                                     roi_bottom_right[1] - roi_top_left[1]))

screenshot_cv1 = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2GRAY)
template1 = cv.imread('jugofwine.png', cv.IMREAD_GRAYSCALE)

result = cv.matchTemplate(screenshot_cv1, template1, cv.TM_CCOEFF_NORMED)

threshold = 0.4

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

# roi_top_left = (553, 377)
# roi_bottom_right = (737, 489)

# screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
#                                      roi_bottom_right[0] - roi_top_left[0], 
#                                      roi_bottom_right[1] - roi_top_left[1]))

# screenshot_cv1 = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2GRAY)
# template1 = cv.imread('jugofwine.png', cv.IMREAD_GRAYSCALE)


# result = cv.matchTemplate(screenshot_cv1, template1, cv.TM_CCOEFF_NORMED)

# threshold = 0.45

# locations = np.where(result >= threshold)

# # Adjust the match locations to the actual screen coordinates
# match_locations = zip(*locations[::-1])
# adjusted_locations = [(pt[0] + roi_top_left[0], pt[1] + roi_top_left[1]) for pt in match_locations]

# # Print the adjusted locations and corresponding match values
# for pt in adjusted_locations:
#     print("Match found at:", pt)
#     print("Match value:", result[pt[1] - roi_top_left[1], pt[0] - roi_top_left[0]])
# Get the location of the best match
#_, max_val, _, _ = cv.minMaxLoc(result)

#     # Check if the maximum match value is above the threshold
# if max_val >= threshold:
#     print("Match found! hittade en jar")
#     print("Max value:", max_val)
        
# else:
#     print("No match found, now we gotta do something")
#     print("Max value:", max_val)
    


# cv.imshow("test", screenshot_cv1)
# cv.waitKey(0)
# cv.destroyAllWindows()




# while True:
#     detect_coin_pouches()
#     detect_hp()
#     ardyknight()







# göra en funktion som kollar jugs of wine i inventoryn och 
# dricker en. 
# roi = 553 377 - 737 489 
# 
#
#
#
#
#
#












# print("checking hp..")
# # Define the region of interest (ROI) coordinates
# roi_top_left = (525, 83)
# roi_bottom_right = (543, 95)
 
# screenshot = aut.screenshot(region=(roi_top_left[0], roi_top_left[1], 
#                                     roi_bottom_right[0] - roi_top_left[0], 
#                                     roi_bottom_right[1] - roi_top_left[1]))

# # Convert the screenshot to OpenCV format (BGR)
# screenshot_cv = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

# # Convert the screenshot to grayscale
# grayscale_img = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

# # Load the template image
# template = cv.imread('hp.png', cv.IMREAD_GRAYSCALE)
# blur = cv.blur(grayscale_img, (3,3))
# blur1 = cv.blur(template, (3,3))
# canny = cv.Canny(blur, 125, 175)

# canny1 = cv.Canny(blur1, 125, 175)

# # cv.imshow("1", canny)
# # cv.imshow("2", canny1)
# # Perform template matching
# result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED)

# # Define a threshold for the match
# threshold = 0.4

# # Get the location of the best match
# _, max_val, _, _ = cv.minMaxLoc(result)
# print(max_val)
# cv.waitKey(0)
# cv.destroyAllWindows()