from Elevator import *
from Passanger import *
from Movement import *
import time

class Manager:
    def __init__(self):
        self.floors = []
        self.passengers = []
        self.requests =[]
        self.currtime = 0
        self.elevator = Elevator()
        self.movement = Movement()
        
        
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
        # self.move(p.floor,self.elevator)
        
        # #then add the passenger
        # self.addPassenger(p,self.elevator)
        # #then satisfy the inner request
        # self.move(p.request,self.elevator)
        # self.remove_passenger(p)
        # time.sleep(3)
        while self.passengers:
            for p in self.passengers:
            #add the request to movement lists and if the passenger is at the same floor of our elevator add the passenger imediatly
                if not self.floorDirection(self.elevator.current,p.floor):
                    self.addPassenger(p,self.elevator)
                    
                self.movement.move()
                
            
            
    
    def floorDirection(self,current, floor):
        if (current > floor):
            self.movement.MovingTowardsDown.append(floor)
            return -1
        elif current<floor:
            self.movement.MovingTowardsUp.append(floor)
            return 1
        else :
            return 0
        

    
    def addPassenger(self,passenger, elevator):
        passenger.status ='onBoard'
        print('im on board!!!! i want to go to ',passenger.request)
        passenger.floor=-1
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
                    


m = Manager()
m.manager()