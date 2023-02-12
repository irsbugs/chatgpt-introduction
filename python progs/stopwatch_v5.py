"""
1. Create a stopwatch class.
2. In the class provide the methods: start and stop.
3. Provide a loop.
4. Display elapsed time.
"""

import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()

    def elapsed_time(self):
        return self.stop_time - self.start_time

stopwatch = Stopwatch()
stopwatch.start()

# loop
for i in range(1,1000000):
    j=i*i

stopwatch.stop()

print("Elapsed Time: %s seconds" % stopwatch.elapsed_time())
