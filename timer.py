import time

def timer():
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"Duration: {elapsed_time:.2f} seconds", end="\r")  # \r to overwrite the previous line
        time.sleep(1)

timer()


