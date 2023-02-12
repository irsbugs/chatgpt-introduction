# write a gui clock program for a computer

import tkinter
from time import strftime

#Create a window
window = tkinter.Tk()
window.title("Digital Clock")
window.geometry("400x100")

#Create a label to display time
clock = tkinter.Label(window, font=("times", 30, "bold"), bg="green")
clock.grid(row=1, column=1, padx=5, pady=5)

def tick():
    time2 = strftime('%H:%M:%S %p')
    clock.config(text=time2)
    clock.after(200, tick)

tick()
window.mainloop()
