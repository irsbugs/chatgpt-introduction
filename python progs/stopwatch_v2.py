# write a stopwatch program with start, stop and reset commands in python

# create a class for the stopwatch
class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.is_running = False
 
    # start the stopwatch
    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
 
    # stop the stopwatch
    def stop(self):
        if self.is_running:
            self.stop_time = time.time()
            self.is_running = False
 
    # reset the stopwatch
    def reset(self):
        self.start_time = 0
        self.stop_time = 0
        self.is_running = False
 
    # get the elapsed time
    def elapsed_time(self):
        if self.is_running:
            return time.time() - self.start_time
        else:
            return self.stop_time - self.start_time
            
print(Stopwatch.start(0))                  
print(Stopwatch.stop)
print(Stopwatch.elapsed_time)   
