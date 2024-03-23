import time
import threading
import pyautogui as aut

def timer():
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"Duration: {elapsed_time:.2f} seconds", end="\r")  # \r to overwrite the previous line
        time.sleep(1)
        if elapsed_time >= 6 * 3600:  # 6 hours * 3600 seconds per hour
            print("Time limit reached. Stopping execution.")
            exit()  # or sys.exit() if you need to exit from a function or module

def ta():
    while True:
        start_time = time.time()

        # Your ta function code goes here
        # Example code:
        aut.moveTo(925, 194) #thieving platsen 
        time.sleep(0.6)
        aut.click()
        aut.moveTo(1155, 253) #inventory 
        aut.keyDown("shift")
        time.sleep(2)
        aut.click()
        aut.keyUp("shift")

        # Check elapsed time
        elapsed_time = time.time() - start_time

        # If 6 hours is reached, break out of the loop
        if elapsed_time >= 6 * 3600:  # 6 hours * 3600 seconds per hour
            print("Time limit reached. Stopping execution.")
            break

# Create and start a thread for the timer
timer_thread = threading.Thread(target=timer)
timer_thread.start()

# Call the ta function
ta()