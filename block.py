import math


class Block:
    def __init__(self):
        self.target_reached = False
        self.target = (500, 500)
        self.color = (0, 255, 0, 128)
        self.size = (40, 40)
        self.move_set = []
        self.position = [0, 0]
        self.fitness = -1
        self.normalized_fitness = 0

    def evaluate(self):
        dx = self.target[0] - self.position[0]
        dy = self.target[1] - self.position[1]
        if dx == 0 and dy == 0:
            self.fitness = 1.0
        else:
            self.fitness = 1 / math.sqrt((dx * dx) + (dy * dy))

    def move(self, frame_count):
        if not self.target_reached:
            self.position[0] += self.move_set[frame_count][0]
            self.position[1] += self.move_set[frame_count][1]

            if self.position[0] == self.target[0] and self.position[1] == self.target[1]:
                self.target_reached = True
                self.color = (0, 0, 255, 128)
