from random import randint
class Passanger:
    def __init__(self):
        self.request = None
        self.status = 'waiting'
        self.floor= randint(0,14)
        if (self.status =='onBoard') :
            self.request=randint(0,14)
            

