#write a gtk qui python program to find square root of X

#import required modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import math

#method to calculate square root
def calculate_sqrt(entry):
    try:
        #convert input to float
        num = float(entry.get_text())
        #calculate square root
        result = math.sqrt(num)
        #set result in label
        label.set_label(str(result))
    except ValueError:
        label.set_label("Invalid input.")

 
#create window
window = Gtk.Window(title="Find Square Root")
#window.set_position(Gtk.WIN_POS_CENTER)
window.set_size_request(250, 100)
 
#create entry for input
entry = Gtk.Entry()
entry.set_max_length(50)
entry.connect("activate", calculate_sqrt)
entry.set_text("Enter a number")
entry.set_size_request(120, 30)
 
#create label for output
label = Gtk.Label()
 
#create a vertical box
vbox = Gtk.VBox()
vbox.pack_start(entry, True, True, 0)
vbox.pack_start(label, True, True, 0)
 
#add box to window
window.add(vbox)
 
#show window
window.show_all()
 
#main loop
Gtk.main()
# No quit Gtk.main_quit()
