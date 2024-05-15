import os
import json
from datetime import *

log_events = ['Fileheader', 'Commander', 'Materials', 'Rank', 'Progress', 'Reputation', 'EngineerProgress',
               'ShipyardSwap', 'ApproachBody', 'ShieldState', 'Touchdown', 'LaunchSRV', 'MaterialDiscovered', 
               'ShipTargeted', 'DockSRV', 'Liftoff', 'LeaveBody', 'Market', 'MissionAccepted', 'MissionCompleted',
               'LoadGame', 'Statistics', 'ReceiveText', 'FSSSignalDiscovered', 'Location', 'ShipLocker', 
               'Missions', 'SAASignalsFound', 'Loadout', 'Cargo', 'Undocked',  
               'Docked', 'StartJump', 'SupercruiseEntry', 'SAAScanComplete', 'ScanBaryCentre', 'Scan', 'NavRoute', 'FSDTarget',
               'NavRouteClear', 'FSDJump', 'FSSDiscoveryScan', 'ReservoirReplenished', 'FuelScoop', 
               'FSSAllBodiesFound', 'SupercruiseDestinationDrop', 'SupercruiseExit', 'RefuelAll', 'FSSBodySignals', 'Promotion', 
               'SellExplorationData', 'ModuleInfo', 'Shipyard', 'StoredShips', 'Outfitting', 'StoredModules', 'ModuleSell', 
               'ModuleBuy', 'CodexEntry', 'MultiSellExplorationData', 
               'Bounty', 'UnderAttack', 'RedeemVoucher', 
               'RepairAll', 'BuyAmmo', 'MaterialCollected', 'Shutdown']

class SessionDump:
    def __init__(self,logfile):

        self.json_log = []  
        new_events = []
        self.logdir=os.getcwd()+os.sep+"log"+os.sep
        fd = open(self.logdir + logfile)

        while line := fd.readline():
            js_line = json.loads(line)
            event = js_line["event"]
            if (event in log_events):
                 self.json_log.append(js_line)
            else :
                if (event not in log_events) and (event not in new_events):
                    new_events.append(event)
        print("----> New events : "+ str(new_events))

        fd.close()       
           

    def printLogEventsList(self):
        self.ev_list = [{'event':'Location', 'num':0}]
        self.ev_list.append({'event':'Bounty', 'num':0})
        for js_line in self.json_log :
            event = js_line["event"]
            for index in range(len(self.ev_list)) :
                js_event = self.ev_list[index]
                if js_event['event'] == event :
                    js_event['num'] += 1
                    break
                elif index == len(self.ev_list)-1:
                    self.ev_list.append({'event':event,'num':1})
                    
        print(self.ev_list)

    #   :   getEvents - Returns named eventsin a list

    def getEvents(self, log_event):
        req_events=[]
        for js_line in self.json_log:
            if js_line['event']== log_event :
                req_events.append(js_line)
        return(req_events)

    def sessionSummary(self):
        # Finding session start and reputation
        str_time="%Y-%m-%dT%H:%M:%SZ"
        js_log=self.json_log
        js_fileHeader = self.getEvents('Fileheader')
        start_date = datetime.strptime(js_fileHeader[0]['timestamp'], str_time)
        print ("Session started at : " + str(start_date))
        print("first event : \n"+ str(self.ev_list[0]))
        for session in js_log:
            print("Event : " + session['event'] + " - " + str(datetime.strptime(session['timestamp'], str_time)))
        print (js_log[0])



if __name__ == "__main__" :
    print("in __main__")
    tst=SessionDump("Journal.2024-05-12T173005.01.log")
    print("cwd = " + tst.logdir)
    print(" -----------------------> Events in file :")
    tst.printLogEventsList()
    req_events = tst.getEvents('Fileheader')
    if len(req_events) > 0 :
        print(json.dumps(req_events[0],indent=4))

    print(" -----> Session summary")
    tst.sessionSummary()

