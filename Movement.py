from Elevator import*
from Manager import*

class Movement:
    def __init__(self):
        self.MovingTowardsUp = []
        self.MovingTowardsDown = []
        self.elevator = Elevator()
        self.manager = Manager()
            
    def moveup(self):
        while True:
            self.manager.currtime += 5 * self.distance(self.elevator.current , self.MovingTowardsUp[0])
            self.elevator.current = self.MovingTowardsUp[0]
            self.elevator.direction=1
            self.MovingTowardsUp.remove(0)
            if not self.MovingTowardsUp and not self.MovingTowardsDown:
                break
            elif not self.MovingTowardsUp:
                self.movedown()
                
    def distance(self,fl1,fl2):
        print('in distance ',fl1,fl2)
        return abs(fl2-fl1)
    
    
    def movedown(self):
        while True:
            self.manager.currtime += 5 * self.distance(self.elevator.current , self.MovingTowardsDown[0])
            self.elevator.current = self.MovingTowardsDown[0]
            self.elevator.direction=-1
            self.MovingTowardsDown.remove(0)
            if not self.MovingTowardsUp and not self.MovingTowardsDown:
                break
            elif not self.MovingTowardsDown:
                self.moveup()
    
    def move(self):
        if abs(max(self.MovingTowardsUp)) > abs(min(self.MovingTowardsDown)):
            self.moveup()
            
        else:
            self.movedown()