#write a gui clock program in python

import tkinter 
import time 

# Create a window 
root = tkinter.Tk() 

# Set window title 
root.title("Clock") 

# Set window size 
root.geometry("350x200") 

# Create a label for clock 
clock = tkinter.Label(root, font = ('times', 20, 'bold'), bg = 'green') 

# Place the label at a particular location 
clock.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER) 

# Function used to update the time display as time changes 
def update_time(): 
	current_time = time.strftime("%H:%M:%S") 
	clock.configure(text = current_time) 
	clock.after(200, update_time) 

update_time() 

# Run the main loop 
root.mainloop()

