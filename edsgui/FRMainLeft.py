import json
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class EventsTreeView :

    def __init__(self, master, container):

        
        self.master = master    #       :       master application for callbacks

  

if __name__ == "__main__" :

    class Example(Gtk.ApplicationWindow):

        def __init__(self, *args, **kwargs):

            print(" kargs : " + str(args))
            print(" kwargs : " + str(kwargs))
            super().__init__(*args,**kwargs)
            
            self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_child(self.box1)
            self.box1.append(self.box2)
            self.box1.append(self.box3)
            self.box1.set_spacing(3)
            print("box1 vexpand : " +str(Gtk.Widget.get_vexpand(self.box1)))
            print("box2 vexpand : " +str(Gtk.Widget.get_vexpand(self.box2)))
            print("spacing : " + str(self.box2.get_spacing()))
            print("homogeneous : " + str(self.box2.get_homogeneous()))
            print("baseline : "+ str(self.box2.get_baseline_position()))
            self.box2.set_baseline_position(Gtk.BaselinePosition.BOTTOM)
            self.box2.set_homogeneous(False)
            self.box2.set_spacing(3)

            self.button1= Gtk.Button(label="Cliquez moi")
            self.box2.append(self.button1)
            self.box2.append(Gtk.Button(label="Cliquez moi - box 1"))
            print("Button1 vexpand : " +str(Gtk.Widget.get_vexpand(self.button1)))
            
            self.box3.append(Gtk.Button(label="Cliquez moi - box 2"))
            self.box3.append(Gtk.Button(label="Cliquez moi - box 2"))
            self.box3.set_spacing(5)

            ev_tree_view = EventsTreeView(None, self.box2)
            
            js_log = []  
            logfile="./log/Journal.2024-05-12T173005.01.log"
            fd = open(logfile)
            for i in range(0,10):
                line = fd.readline()
                js_log.append(json.loads(line))
            print(json.dumps(js_log[0],indent=4))
            ev_tree_view.event_list_replace(js_log)
            

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