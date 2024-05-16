import json
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class LeftPanel :

    def __init__(self, master, container):
        
        self.master = master    #       :       master application for callbacks - transmit to widgets

        exp_settings = Gtk.Expander(label="Settings")
        exp_session = Gtk.Expander(label="Session")

        bx_settings = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        exp_settings.set_child(bx_settings)

        bx_settings.append(Gtk.Label(label="Post Session"))
        bx_settings.append(Gtk.Label(label="log dir : <logdir>"))
        bx_settings.append(Gtk.Label(label="log file : <logfile>"))
        bx_settings.append(Gtk.Button(label="change"))

        bx_session = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        bx_session.append(Gtk.Button(label="change"))
        exp_session.set_child(bx_session)

        bx_session.append(Gtk.Label(label="< SESSION TREE VIEW >"))

        container.append(bx_settings)
        container.append(bx_session)


  

if __name__ == "__main__" :

    class Example(Gtk.ApplicationWindow):

        def __init__(self, *args, **kwargs):

            print(" kargs : " + str(args))
            print(" kwargs : " + str(kwargs))
            super().__init__(*args,**kwargs)
            
            self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box2)
 
            self.box2.set_baseline_position(Gtk.BaselinePosition.TOP)
            self.box2.set_homogeneous(False)
            self.box2.set_spacing(3)

            left_panel=LeftPanel(None,self.box2)
            self.set_child(self.box2)
            

    class TestUnit(Adw.Application):
        def __init__(self, **kwargs):
            print("myapp kwargs : "+str(kwargs))
            super().__init__(**kwargs)
            self.connect('activate', self.on_activate)

        def on_activate(self, app):
            self.win = Example(application=app)
            self.win.present()

    #       :   ----------------------------------------------------------
    #       :       CallBacks section.
    #       :       Contained callback methods to be used by GUI widgets
    #       :       used to interact with application

    #       :   
    #       :   guiEventsTreeCallback - callback method for Events TreeBox selection.
    #       :

        def guiEventsTreeCallback (js_event) :
            print("--- selected event : " + json.dumps(js_event))

    app = TestUnit(application_id="lab.example.GtkApplication")
    app.run()