import math


class Block:
    def __init__(self):
        self.target_reached = False
        self.color = (0, 255, 0, 128)
        self.size = (40, 40)
        self.move_set = []
        self.position = [0, 0]
        self.fitness = -1
        self.bonus = 0

    def evaluate(self, target):
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        if dx <= 0 and dy <= 0:
            self.fitness = 1.0 + self.bonus
        else:
            self.fitness = 1 / math.sqrt((dx * dx) + (dy * dy))

    def move(self, count, target):
        if not self.target_reached:
            self.position[0] += self.move_set[count][0]
            self.position[1] += self.move_set[count][1]

            if self.position[0] > target[0] and self.position[1] > target[1]:
                self.target_reached = True
                self.color = (0, 0, 255, 128)
                self.bonus = len(self.move_set) - count
