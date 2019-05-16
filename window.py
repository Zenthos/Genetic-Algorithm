import pygame
import time
import sys
pygame.init()


class Screen:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SRCALPHA)
        self.font = pygame.font.SysFont("Arial", 16)
        self.frames = 0
        self.count = 0
        self.time_at_run = time.process_time()
        self.colors = {"RED": [255, 0, 0, 10],
                       "GREEN": [0, 255, 0, 128],
                       "BLUE": [0, 0, 255, 128],
                       "WHITE": [255, 255, 255],
                       "BLACK": [0, 0, 0]}

    def setup(self):
        self.screen.fill(self.colors["BLACK"], (0, 0, self.screen_width, self.screen_height))
        pygame.display.set_caption("Smart Blocks")

    def calc_fps(self, population):
        self.count += 1
        if self.count % population.max_moves == 0:
            t1 = time.process_time()
            self.frames = 500 / (t1 - self.time_at_run)
            self.time_at_run = t1
            self.count = 0
            population.perform_ga()
            population.generation += 1

    def draw_blocks(self, population):
        for block in population.population:
            block.move(self.count)

        for block in population.population:
            self.screen.fill(block.color, (block.position[0], block.position[1], block.size[0], block.size[1]))

        self.screen.fill(self.colors["RED"], (population.target[0] + 10, population.target[1] + 10, 20, 20), 1)

    def draw_text(self, population):
        frame_count = self.font.render("Frame = {0} fps Generation: {1}".format(self.count, population.generation), True, (255, 255, 255))
        frame_rate = self.font.render("Frame_rate = {0:.2f}".format(self.frames), True, self.colors["WHITE"])
        fitness_text = self.font.render("Average Fitness: {0}".format(population.avg_fit), True, self.colors["WHITE"])

        self.screen.blit(fitness_text, (self.screen_width - 250, 10))
        self.screen.blit(frame_count, (self.screen_width - 250, 40))
        self.screen.blit(frame_rate, (self.screen_width - 250, 70))

    @staticmethod
    def exit():
        pygame.quit()
        sys.exit()
