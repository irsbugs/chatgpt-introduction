"""
1. Create a stopwatch program.
2. Provide the commands: start, stop and reset.
3. Display time for each command.
"""

import time

print("Welcome to the Stopwatch Program")

# Initialize variable
start_time = None

# Program logic
while True:
    user_input = input("Please enter 'start', 'stop' or 'reset': ")
    if user_input == "start":
        if start_time == None:
            start_time = time.time()
            print("Stopwatch started")
        else:
            print("Stopwatch already started")
    elif user_input == "stop":
        if start_time != None:
            elapsed_time = round(time.time() - start_time, 2)
            start_time = None
            print(f"Stopwatch stopped: {elapsed_time}")
        else:
            print("Stopwatch not started")
    elif user_input == "reset":
        start_time = None
        print("Stopwatch reset")
    else:
        print("Invalid input")


