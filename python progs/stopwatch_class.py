# write a stopwatch program with start, 
# stop and reset commands in python

#importing time module
import time

#defining stopwatch class
class Stopwatch():
    #initializing start time
    start_time = 0.0
    #initializing stop time
    stop_time = 0.0
    #initializing boolean to check if timer is running
    running = False
    
    #defining start method
    def start(self):
        #if timer is already running
        if self.running == True:
            print("The timer is already running")
        #if timer is not running
        else:
            #updating running to true
            self.running = True
            #updating start time
            self.start_time = time.time()
            print("The timer has started")
    
    #defining stop method
    def stop(self):
        #if timer is not running
        if self.running == False:
            print("The timer is already stopped")
        #if timer is running
        else:
            #updating running to false
            self.running = False
            #updating stop time
            self.stop_time = time.time()
            print("The timer has stopped")
    
    #defining reset method
    def reset(self):
        #updating running to false
        self.running = False
        #updating start and stop time to 0
        self.start_time = 0.0
        self.stop_time = 0.0
        print("The timer has been reset")
    
    #defining elapsed time
    def elapsed_time(self):
        #if timer is running
        if self.running == True:
            elapsed_time = time.time() - self.start_time
        #if timer is not running
        else:
            elapsed_time = self.stop_time - self.start_time
        #returning elapsed time
        return elapsed_time

#creating stopwatch object
stopwatch_obj = Stopwatch()

#calling start method
stopwatch_obj.start()

#calling stop method
stopwatch_obj.stop()

#calling reset method
stopwatch_obj.reset()

#calculating elapsed time
elapsed_time = stopwatch_obj.elapsed_time()

#printing elapsed time
print("The elapsed time is:", elapsed_time)
