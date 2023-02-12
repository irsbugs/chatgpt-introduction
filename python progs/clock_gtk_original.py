# write a gtk gui clock proram in python
# Original - Fails to run

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import time

class ClockWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK Clock")
        self.set_border_width(10)
        self.set_default_size(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.label = Gtk.Label("Time will appear here")
        self.add(self.label)

        # Create timeout to update the clock every second 
        GObject.timeout_add(1000, self.update_clock)

    def update_clock(self):
        # Get the current time 
        current_time = time.strftime("%H:%M:%S")
        # Update the label with the current time 
        self.label.set_label(current_time)
        # Return true so the timeout will run again 
        return True

window = ClockWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()


