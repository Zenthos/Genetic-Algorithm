from block import Block
import random


def selection(population):
    population = sorted(population, key=lambda block: block.fitness, reverse=True)
    best_fit = round(0.1 * len(population))
    population = population[:best_fit]
    return population


def cross_over(population, size, max_moves):
    offspring = []

    for _ in range(int(size/2)):
        parents = random.sample(population, 2)
        child1 = Block()
        child2 = Block()

        split = random.randint(0, max_moves)
        child1.move_set = parents[0].move_set[0:split] + parents[1].move_set[split:max_moves]
        child2.move_set = parents[1].move_set[0:split] + parents[0].move_set[split:max_moves]

        offspring.append(child1)
        offspring.append(child2)

    return offspring


def mutation(population, mutation_rate, size, max_moves):
    chance = random.randint(0, 100)
    num_mutated = random.randint(0, size)
    num_moves_mutated = random.randint(o, max_moves)

    if chance >= 100 - mutation_rate:
        for _ in range(num_mutated):
            mutated_block = population[random.randint(0, len(population) - 1)]
            for _ in range(num_moves_mutated):
                rand_x = random.randint(-1, 1)
                rand_y = random.randint(-1, 1)
                mutated_block.move_set[random.randint(0, max_moves - 1)] = [rand_x, rand_y]

    return population
