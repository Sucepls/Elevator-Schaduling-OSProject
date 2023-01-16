from Elevator import *
from Passanger import *

class manager:
    def __init__(self):
        self.floors = []
        self.passengers = []
        self.requests =[]
        self.currtime = 0
        self.elevator = Elevator()
        
        
    #main core to generate passengers
    def manager(self):
        while True:
            print ("   Welcome to the building     ")
            print("    current time is: ",self.currtime,"   ")
            print("    current floor is: ",self.elevator.current,"   ")
            p = Passanger()
            self.passengers.append(p)
            self.outRequests()
            self.mainAlgorithm(p)
            
            
        
    # def algorithm to choose witch request to responce
    def mainAlgorithm(self,p):
            #first satisfy the request
        self.move(p.floor,self.elevator)
        
            #then add the passenger
        self.addPassenger(p,self.elevator)
            #then satisfy the inner request
        self.move(p.request,self.elevator)
        self.remove_passenger(p)
            
            
            
    
    def floorDirection(current, floor):
        if (current > floor):
            return -1
        elif current<floor:
            return 1
        else :
            return 0
        
    def distance(self,fl1,fl2):
        print(fl1,fl2)
        tmp=fl2-fl1
        return abs(tmp)
    
    def addPassenger(self,passenger, elevator):
        passenger.status ='onBoard'
        elevator.passengers.append(passenger)
        #inner request are added here
        self.requests.append(passenger.request)
        #1 time unit will pass to add a passenger
        self.currtime += 1
    
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
        
        #1 time unit will pass to remove a passenger
        self.currtime += 1
        
        
    def outRequests(self):
        for pas in self.passengers:
            if pas.status == 'waiting':
                self.requests.append(pas.floor)
                    
    def move(self,req , elevator):
        print('here')
        #10 time unit will be spent to go from a floor to another
        self.currtime += 5 * self.distance(elevator.current , req)
        
        elevator.current = req
        self.requests.remove(req)


m = manager()
m.manager()