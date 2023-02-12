#write a gtk qui python program to find square root of X

#import required modules
import gtk
import math
 
#create window
window = gtk.Window(title="Find Square Root")
window.set_position(gtk.WIN_POS_CENTER)
window.set_size_request(150, 100)
 
#create entry for input
entry = gtk.Entry()
entry.set_max_length(50)
entry.connect("activate", calculate_sqrt)
entry.set_text("Enter a number")
entry.set_size_request(120, 30)
 
#create label for output
label = gtk.Label()
 
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
 
#create a vertical box
vbox = gtk.VBox()
vbox.pack_start(entry, True, True, 0)
vbox.pack_start(label, True, True, 0)
 
#add box to window
window.add(vbox)
 
#show window
window.show_all()
 
#main loop
gtk.main()
