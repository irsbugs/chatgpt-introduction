# write a gtk gui clock proram in python
# Updated

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib 
import time

class ClockWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK Clock")
        self.set_border_width(10)
        self.set_default_size(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.label = Gtk.Label(label="Time will appear here")
        self.add(self.label)

        # Create timeout to update the clock every second 
        GLib.timeout_add(1000, self.update_clock)

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


"""
# With maximum length set to 1000. Before at 256 program was truncated

WARNINGS:
progs/clock_gtk.py:21: PyGIDeprecationWarning: GObject.timeout_add is deprecated; use GLib.timeout_add instead
  GObject.timeout_add(1000, self.update_clock)

...changed to
        GLib.timeout_add(1000, self.update_clock)

progs/clock_gtk.py:17: PyGTKDeprecationWarning: Using positional arguments with the GObject constructor has been deprecated. Please specify keyword(s) for "label" or use a class specific constructor. See: https://wiki.gnome.org/PyGObject/InitializerDeprecations
  self.label = Gtk.Label("Time will appear here")
...changed to:
 self.label = Gtk.Label(label="Time will appear here")
"""


"""
#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import time

class ClockApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK Clock")

        self.set_border_width(10)
        self.set_size_request(200, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.label = Gtk.Label()
        self.label.set_markup("<span font_desc='Sans Bold 60'>00:00:00</span>")
        vbox.pack_start(self.label, True, True, 0)

        button = Gtk.Button(label="Quit")
        #button.connect("clicked", self.on_clicked_quit)
        vbox.pack_start(button, True, True, 0)
        
        
        
        #win.set_child(btn)
        #win.present()

# Added
win = ClockApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


#app = Gtk.Application(application_id='org.gtk.Example')
#app.connect('activate', on_activate)
#app.run(None)

"""
