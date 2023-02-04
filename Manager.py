from Elevator import Elevator


class Manager:
    def __init__(self):
        self.arr = 0
        self.head = 7
        self.elevator = Elevator()
        self.direction = "waiting"

    def app(self, req):
        if not self.elevator.down and not self.elevator.up:
            if req > self.head:
                self.direction = "up"
            elif req < self.head:
                self.direction = "down"
        self.arr = req
        self.elevator.optimation(self.arr, self.direction)

    def getinput(self):
        try:
            while True:
                Frequest = input("What request do you have?")
                self.app(int(Frequest))
        except:
            self.getinput()


if __name__ == "__main__":
    m = Manager()
    m.getinput()
