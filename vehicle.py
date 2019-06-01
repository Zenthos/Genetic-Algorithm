import math
import pymunk
import pymunk.pygame_util
import pymunk.util
import pygame


class Arrow:
    def __init__(self, screen):
        self.mass = 1
        self.bonus = 0
        self.fitness = 0
        self.angle = []
        self.velocity = []
        self.color = (0, 255, 0, 200)
        self.position = (30, 300)
        self.target_reached = False
        self.vertices = [(15, 8), (15, -8), (-15, 0)]
        self.vertices = [pymunk.pygame_util.from_pygame(point, screen) for point in self.vertices]
        self.vertices = pymunk.util.poly_vectors_around_center(self.vertices)
        self.inertia = pymunk.moment_for_poly(self.mass, self.vertices)
        self.body = pymunk.Body(self.mass, self.inertia)
        self.body.position = pymunk.pygame_util.from_pygame(self.position, screen)
        self.body.angle = math.pi
        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.filter = pymunk.ShapeFilter(categories=0b100, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0b100)

    def draw(self, screen):
        vertices = [point.rotated(self.body.angle) + self.body.position for point in self.shape.get_vertices()]
        vertices = [pymunk.pygame_util.to_pygame(point, screen) for point in vertices]
        pygame.draw.polygon(screen, self.color, vertices, 0)

    def evaluate(self, p, screen):
        self.position = pymunk.pygame_util.to_pygame(self.body.position, screen)
        target = pymunk.pygame_util.to_pygame(p.target_body.position, screen)
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        if self.target_reached:
            self.fitness = 1.0 + self.bonus
        else:
            self.fitness = 1 / math.hypot(dx, dy)

    def move(self, p):
        if not self.target_reached and p.lifespan < 1000:
            self.body.angle += self.angle[p.lifespan]
            self.body.velocity = -self.velocity[p.lifespan][0]*math.cos(self.body.angle), -self.velocity[p.lifespan][1]*math.sin(self.body.angle)
        else:
            self.body.velocity = 0, 0
            self.body.angular_velocity = 0

        if self.target_reached:
            self.body.position = p.target_body.position

    def target_collided(self, p, finished_shapes):
        if self.shape in finished_shapes and not self.target_reached:
            self.target_reached = True
            self.bonus = p.max_moves - p.lifespan
