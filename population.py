from block import Block
import random
import ga


class Population:
    def __init__(self):
        self.size = 20
        self.max_moves = 1500
        self.mutation_rate = 30
        self.target = (500, 500)
        self.population = []
        self.generation = 0
        self.avg_fit = 0

    def create_population(self):
        new_population = []
        # Create the first population
        for block in range(self.size):
            new_population.append(Block())

        # Generate the move set for the population
        for block in new_population:
            for _ in range(self.max_moves + 1):
                rand_x = random.randint(-1, 1)
                rand_y = random.randint(-1, 1)
                block.move_set.append([rand_x, rand_y])

        self.population = new_population

    def perform_ga(self):
        self.calc_fit()
        self.calc_avg_fit()
        self.population = ga.selection(self.population)
        self.population = ga.cross_over(self.population, self.size, self.max_moves)
        self.population = ga.mutation(self.population, self.mutation_rate, self.size, self.max_moves)

    def calc_fit(self):
        for block in self.population:
            block.evaluate()

    def calc_avg_fit(self):
        avg_sum = sum(block.fitness for block in self.population)
        self.avg_fit = avg_sum / self.size
