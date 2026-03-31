from pynput.keyboard import Controller, Key
import pygetwindow as gw
import time

# Create a controller to simulate key events
keyboard = Controller()

# Get a list of all open RuneLite windows
windows = gw.getWindowsWithTitle("RuneLite -")

if len(windows) < 2:
    print("At least two RuneLite windows must be open!")
    exit()

# Print the names of the windows found
print(f"Found windows: {[window.title for window in windows]}")

# Activate and focus on each window
for window in windows:
    window.activate()  # Bring the window to focus
    print(f"Focusing on window: {window.title}")
    time.sleep(1)  # Wait a bit before sending the key release

    # Simulate key press down (Up Arrow key) and key release (keyup)
    keyboard.press(Key.up)  # Simulate pressing down the Up Arrow key
    time.sleep(0.1)  # Simulate the press duration
    keyboard.release(Key.up)  # Simulate releasing the Up Arrow key (keyup)
    time.sleep(0.1)  # Slight delay before moving to the next window

print("Key release sent to all windows!")