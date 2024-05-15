import json
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class EventsTreeView :

    def __init__(self, master, container):

        
        self.master = master    #       :       master application for callbacks

        #       :       Creating the TreeStore and populating it

        self.tree_store = Gtk.TreeStore(str, str)

        #       :   Initializing events list
        list_events=None
        if list_events != None :
            for event in list_events :
                self.tree_store.append(None,[json.loads(event)['event'],event])

        #       :       Creating Column/Renderer for display - only one is displayed

        col1 = Gtk.TreeViewColumn("Event List", Gtk.CellRendererText(), text=0)
        # col2 = Gtk.TreeViewColumn("Col2") # no renderer 

        #       :       Creating TreeView, adding column and mapping change event
        self.tree_view = Gtk.TreeView(model = self.tree_store)
        self.tree_view.append_column(col1)
        Gtk.Widget.set_vexpand(self.tree_view,True)   # We want the tree to extend to bottom of the box.
        select = self.tree_view.get_selection()
        select.connect("changed", self.on_tree_selection_changed)

        #       :   Creating a scrolled window for the TreeView

        self.scroll_tree=Gtk.ScrolledWindow()
        self.scroll_tree.set_child(self.tree_view)

        container.append(self.scroll_tree)
        

    #       :
    #       :   Method called as a Tree item is selected.
    #       :

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print("You selected" + str(model[treeiter][1]))

    def event_append(self, event):
        self.tree_store.append(None, [event['event'],event])

    def event_list_replace(self, event_list=[]):
        if event_list != None:
            self.tree_store.clear()
            self.tree_view.set_model(None)  #  Removing data display during update (for performance)
            for event in event_list :
                print("Event name : " + event['event'])
                self.tree_store.append(None,[event['event'],json.dumps(event)])
            self.tree_view.set_model(self.tree_store)  #  Restoring data model.



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
        logfile="/home/bgillet/DEV/python/Elite_Dangerous/log/Journal.2024-05-12T173005.01.log"
        fd = open(logfile)
        for i in range(0,10):
            line = fd.readline()
            js_log.append(json.loads(line))
        print(json.dumps(js_log[0],indent=4))
        ev_tree_view.event_list_replace(js_log)
            
        



        




class MyApp(Adw.Application):
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

app = MyApp(application_id="lab.example.GtkApplication")
app.run()