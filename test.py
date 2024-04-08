import cv2
import numpy as np
from PIL import ImageGrab

# Function to convert PIL image to OpenCV format
def pil_to_cv(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Initialize background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Main loop
while True:
    # Capture screen
    screen = ImageGrab.grab()

    # Convert PIL image to OpenCV format
    frame = pil_to_cv(screen)

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Find contours of moving objects
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding box around moving objects
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Adjust threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Close windows
cv2.destroyAllWindows()