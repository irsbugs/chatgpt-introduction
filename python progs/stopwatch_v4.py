"""
1. Create a stopwatch class.
2. In the class provide the methods: start, stop and reset.
3. Provide a loop.
4. Display elapsed time.
"""

import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()
        self.elapsed_time = self.stop_time - self.start_time

    def reset(self):
        self.start_time = 0
        self.stop_time = 0
        self.elapsed_time = 0

stopwatch = Stopwatch()

while True:
    try:
        print("1. Start\n2. Stop\n3. Reset\n4. Exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            stopwatch.start()
        elif choice == 2:
            stopwatch.stop()
            print("Elapsed time: %.2f seconds." % stopwatch.elapsed_time)
        elif choice == 3:
            stopwatch.reset()
            print("Stopwatch has been reset.")
        elif choice == 4:
            break
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")
        
