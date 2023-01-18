# from Elevator import*


# class Movement:
#     def __init__(self):
#         self.MovingTowardsUp = []
#         self.MovingTowardsDown = []
#         self.RequestKindUP =[] #if its and inner request 1 otherwise 0
#         self.RequestKindDown =[]
#         self.elevator = Elevator()
#         self.time=0
            
#     def moveup(self):
#         while self.MovingTowardsUp:
#             self.time += 5 * self.distance(self.elevator.current , self.MovingTowardsUp[0])
#             self.elevator.current = self.MovingTowardsUp[0]
#             print("ELEVATOR IS IN ", self.elevator.current)
#             self.elevator.direction=1
#             self.MovingTowardsUp.remove(self.elevator.current)
#             if not self.MovingTowardsUp and not self.MovingTowardsDown:
#                 break
#             elif not self.MovingTowardsUp:
#                 self.movedown()
                
#     def distance(self,fl1,fl2):
#         print('in distance calculating between...',fl1,fl2)
#         return abs(fl2-fl1)
    
    
#     def movedown(self):
#         while self.MovingTowardsDown:
#             self.time += 5 * self.distance(self.elevator.current , self.MovingTowardsDown[0])
#             self.elevator.current = self.MovingTowardsDown[0]
#             print("ELEVATOR IS IN ", self.elevator.current)
#             self.elevator.direction=-1
#             self.MovingTowardsDown.remove(self.elevator.current)
#             if not self.MovingTowardsUp and not self.MovingTowardsDown:
#                 break
#             elif not self.MovingTowardsDown:
#                 self.moveup()
    
#     def move(self):
#         if not self.MovingTowardsUp and not self.MovingTowardsDown:
#             print('no request')
#             return
#         elif not self.MovingTowardsUp:
#             self.movedown()
#             print("no up request")
#         elif not self.MovingTowardsDown or (abs(max(self.MovingTowardsUp)) > abs(min(self.MovingTowardsDown))):
#             self.moveup()
            
#         else:
#             self.movedown()