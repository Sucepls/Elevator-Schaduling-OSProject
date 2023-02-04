import threading
import time


class Elevator (threading.Thread):

    def __init__(self):
        super().__init__()
        self.down = []
        self.up = []
        self.seek_sequence = []
        self.head = 7
        self.counter = 0
        self.start()

    def optimation(self, arr, direction):
        if arr < self.head:
            self.down.append(arr)
        if arr > self.head:
            self.up.append(arr)
        self.down.sort(reverse=True)
        self.up.sort()
        run = 2
        while run:
            if direction == "down":
                for i in range(len(self.down)):
                    cur_track = self.down[i]
                    self.seek_sequence.append(cur_track)
                direction = "up"
            elif direction == "up":
                for i in range(len(self.up)):
                    cur_track = self.up[i]
                    self.seek_sequence.append(cur_track)
                direction = "down"
            run -= 1
        if self.counter == 0:
            self.counter += 1
        else:
            for i in range(self.counter):
                self.seek_sequence.pop(0)
            self.counter += 1

    def run(self):
        while True:
            if not self.seek_sequence:
                pass
            elif self.head > self.seek_sequence[0]:
                time.sleep(1)
                self.head -= 1
                print("\n")
                print("head is:", self.head)
                print("--------------------------")
            elif self.head < self.seek_sequence[0]:
                time.sleep(1)
                self.head += 1
                print("\n")
                print("head is:", self.head)
                print("--------------------------")
            elif self.head == self.seek_sequence[0]:
                print("\n")
                print(self.seek_sequence[0], "remove")
                print("--------------------------")
                self.seek_sequence.pop(0)
