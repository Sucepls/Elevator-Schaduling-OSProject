class Elevator:

    def __init__(self):
        self.current = 7
        self.isMoving = False
        self.direction = 0
        self.passangers = []
        self.speed = 10

    def move(self, floor):
        self.current = floor

