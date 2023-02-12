"""
1. Create a stopwatch class.
2. In the class provide the methods: start and stop.
3. provide a menu to select start and stop comands to call class
4. Display elapsed time.
"""

import time

# Create a Stopwatch class
class Stopwatch:
    # Define the start method
    def start(self):
        self.start_time = time.time()

    # Define the stop method
    def stop(self):
        self.stop_time = time.time()
        self.elapsed_time = self.stop_time - self.start_time
    # Define the elapsed time
        self.elapsed_time = round(self.elapsed_time,2)

# Create a menu
def menu():
    print("\nWhat would you like to do?")
    print("1. Start Timer")
    print("2. Stop Timer")
    print("3. Quit")

# Create a main function
def main():
    # Make an instance of the Stopwatch class
    timer = Stopwatch()
    choice = 0
    while choice != 3:
        menu()
        choice = int(input("\nPlease enter your choice: "))
        if choice == 1:
            timer.start()
        elif choice == 2:
            timer.stop()
            print("\nElapsed time: ", timer.elapsed_time)
        elif choice == 3:
            print("\nGoodbye!")

        else:
            print("\nThat is not a valid choice. Please try again!")

# Call the main function
main()

