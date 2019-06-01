import vehicle
import random
import ga
import pymunk


class Population:
    def __init__(self):
        self.size = 20
        self.max_moves = 1000
        self.mutation_rate = 30
        self.target_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.target_shape = pymunk.Circle(self.target_body, 10, (0, 0))
        self.target_body.position = (750, 300)
        self.population = []
        self.generation = 0
        self.avg_fit = 0
        self.lifespan = 0
        self.mutation_happened = False

    def create_population(self, screen, space):
        new_population = []
        # Create the first population
        for arrow in range(self.size):
            a = vehicle.Arrow(screen)
            space.add(a.body, a.shape)
            new_population.append(a)

        for arrow in new_population:
            for _ in range(self.max_moves):
                r = random.uniform(-0.06, 0.06)
                vx = random.randint(-10, 40)
                vy = random.randint(-10, 40)
                arrow.angle.append(r)
                arrow.velocity.append((vx, vy))

        self.population = new_population

    def perform_ga(self, screen, space):
        self.generation += 1
        self.calc_fit(screen)
        ga.selection(self)
        ga.cross_over(self, screen, space)
        ga.mutation(self)

    def calc_fit(self, screen):
        for arrow in self.population:
            arrow.evaluate(self, screen)

        fit_sum = sum(arrow.fitness for arrow in self.population)
        self.avg_fit = fit_sum / self.size

    def check_finishers(self, finished_shapes):
        for arrow in self.population:
            arrow.target_collided(self, finished_shapes)
