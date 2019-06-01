import sys
import pygame
import pymunk.pygame_util


class Frame:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        self.font = pygame.font.SysFont("Arial", 16)
        self.running = True
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.handler = self.space.add_default_collision_handler()
        self.handler.begin = self.begin
        self.shapes_finished = []
        pygame.display.set_caption("Genetic Algorithm 2.0")

    def begin(self, arbiter, space, data):
        self.shapes_finished.append(arbiter.shapes[1])
        return True

    def draw(self, p):
        self.screen.fill((0, 0, 0))
        self.surface.fill((0, 0, 0))

        self.surface.blit(self.font.render("Generation: {}".format(p.generation), True, (255, 255, 255)), (650, 10))
        self.surface.blit(self.font.render("Lifespan: {}".format(p.lifespan), True, (255, 255, 255)), (650, 30))
        self.surface.blit(self.font.render("{}".format(p.avg_fit), True, (255, 255, 255)), (650, 50))
        self.surface.blit(self.font.render("Mutate Happened: {}".format(p.mutation_happened), True, (255, 255, 255)), (650, 70))
        self.surface.blit(self.font.render("FPS: {:.2f}".format(self.clock.get_fps()), True, (255, 255, 255)), (10, 10))

        point = pymunk.pygame_util.to_pygame(p.target_body.position, self.screen)
        pygame.draw.circle(self.surface, (255, 0, 0), point, int(p.target_shape.radius*2), 0)  # Target

        for arrow in p.population:
            arrow.draw(self.surface)

        p.check_finishers(self.shapes_finished)
        self.screen.blit(self.surface, (0, 0))

    def exit(self):
        self.running = False
        pygame.quit()
        sys.exit()
