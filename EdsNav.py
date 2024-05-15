import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

import edsgui.Win as Win

class Launcher(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = Win.GWMainWindow(application=app)
        self.win.present()

app = Launcher(application_id="lab.bjg.edsnav")
app.run(sys.argv)