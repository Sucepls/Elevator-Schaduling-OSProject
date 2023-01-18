from Elevator import *
from Passanger import *
# from Movement import *
import time

class Manager:
    def __init__(self):
        self.floors = []
        self.passengers = []
        self.requests =[]
        self.MovingTowardsUp = []
        self.MovingTowardsDown = []
        self.RequestKindUP =[] #if its and inner request 1 otherwise 0
        self.RequestKindDown =[]
        self.time = 0
        self.elevator = Elevator()
        # self.movement = Movement()
        
        
    #main core to generate passengers
    def manager(self):
        print ("   Welcome to the building     ")
        print("    current time is: ",self.time,"   ")
        print("    current floor is: ",self.elevator.current,"   ")
        p = Passanger()
        p1 = Passanger()
        p2=Passanger()
        p3=Passanger()
        p4=Passanger()
        self.passengers.append(p)
        self.passengers.append(p1)
        self.passengers.append(p2)
        self.passengers.append(p)
        self.passengers.append(p3)
        self.passengers.append(p4)
        # self.outRequests()
        self.mainAlgorithm(p)
            
            
        
    # def algorithm to choose witch request to responce
    def mainAlgorithm(self,p):
        while self.passengers:
            for p in self.passengers:
                print("i am in ",p.floor)
                print("    current time is: ",self.time,"   ")
                print("    current floor is: ",self.elevator.current,"   ")
            #add the request to movement lists and if the passenger is at the same floor of our elevator add the passenger imediatly
                if self.floorDirection(self.elevator.current,p.floor)==0:
                    self.addPassenger(p,self.elevator)
                elif self.floorDirection(self.elevator.current,p.floor)==1:
                    print('he is up')
                    self.MovingTowardsUp.append(p.floor)
                    self.RequestKindUP.append(0)
                else:
                    print('he is down')
                    self.MovingTowardsDown.append(p.floor) 
                    self.RequestKindDown.append(0)
                self.passengers.remove(p)
                time.sleep(3)
            self.move()
            
    
    def floorDirection(self,current, floor):
        if (current > floor):
            
            return -1
        elif current<floor:
            
            return 1
        else :
            return 0
        

    
    def addPassenger(self):
        passenger=Passanger()
        passenger.status ='onBoard'
        passenger.floor=-1
        print('im on board!!!! i want to go to ',passenger.request)
        self.elevator.passengers.append(passenger)
        #inner request are added here
        if self.floorDirection(self.elevator.current,passenger.request):
            print('inner request added')
            self.MovingTowardsUp.append(passenger.request)
            self.RequestKindUP.append(1)
        elif not self.floorDirection(self.elevator.current,passenger.request):
            self.remove_passenger()
        else:
            self.MovingTowardsDown.append(passenger.request) 
            self.RequestKindDown.append(1)
            
        #1 time unit will pass to add a passenger
        self.time += 1
    
    def remove_passenger(self):
        print('i reached my destination at floor: ',self.elevator.current)
        # self.passengers.remove(passenger)
        #1 time unit will pass to remove a passenger
        self.time += 1
        
    #movement stuff   
    def moveup(self):
        while self.MovingTowardsUp:
            self.time += 5 * self.distance(self.elevator.current , self.MovingTowardsUp[0])
            self.elevator.current = self.MovingTowardsUp[0]
            if self.RequestKindUP[0]==0:
                print('here u')
                self.addPassenger()
            else:
                self.remove_passenger()
            self.RequestKindUP.remove(self.RequestKindUP[0])
            print("ELEVATOR IS IN ", self.elevator.current)
            self.elevator.direction=1
            self.MovingTowardsUp.remove(self.elevator.current)
            if not self.MovingTowardsUp and not self.MovingTowardsDown:
                break
            elif not self.MovingTowardsUp:
                self.movedown()
                
    def distance(self,fl1,fl2):
        print('in distance calculating between...',fl1,fl2)
        return abs(fl2-fl1)
    
    
    def movedown(self):
        while self.MovingTowardsDown:
            self.time += 5 * self.distance(self.elevator.current , self.MovingTowardsDown[0])
            self.elevator.current = self.MovingTowardsDown[0]
            if self.RequestKindDown[0]==0:
                print('here d')
                self.addPassenger()
                
            else:
                self.remove_passenger()
            self.RequestKindDown.remove(self.RequestKindDown[0])
            print("ELEVATOR IS IN ", self.elevator.current)
            self.elevator.direction=-1
            self.MovingTowardsDown.remove(self.elevator.current)
            if not self.MovingTowardsUp and not self.MovingTowardsDown:
                break
            elif not self.MovingTowardsDown:
                self.moveup()
    
    def move(self):
        if not self.MovingTowardsUp and not self.MovingTowardsDown:
            print('no request')
            return
        elif not self.MovingTowardsUp:
            self.movedown()
            print("no up request")
        elif not self.MovingTowardsDown or (abs(max(self.MovingTowardsUp)) > abs(min(self.MovingTowardsDown))):
            self.moveup()
            
        else:
            self.movedown()


m = Manager()
m.manager()