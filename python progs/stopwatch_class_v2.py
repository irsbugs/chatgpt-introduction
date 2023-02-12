"""
1. Create a stopwatch class.
2. In the class provide the methods: start and stop.
3. In loop provide start and stop comands to call class
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
        return self.stop_time - self.start_time

stopwatch = Stopwatch()
while True:
    command = input('Type "start" to start the stopwatch or "stop" to stop it: ')
    if command == 'start':
        stopwatch.start()
    elif command == 'stop':
        elapsed_time = stopwatch.stop()
        print('Elapsed time is {} seconds.'.format(elapsed_time))
        break
