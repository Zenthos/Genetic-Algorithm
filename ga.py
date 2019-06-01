from vehicle import Arrow
import random


def selection(p):
    selected = sorted(p.population, key=lambda arrow: arrow.fitness, reverse=True)
    best_fit = round(0.1 * len(selected))
    p.population.clear()
    p.population = selected[:best_fit]


def cross_over(p, screen, space):
    offspring = []

    for arrow in p.population:
        space.remove(arrow.body, arrow.shape)

    for _ in range(int(p.size)):
        parents = random.sample(p.population, 2)

        child = Arrow(screen)
        split = random.randint(0, p.max_moves)
        child.angle = parents[0].angle[0:split] + parents[1].angle[split:p.max_moves]
        split = random.randint(0, p.max_moves)
        child.velocity = parents[0].velocity[0:split] + parents[1].velocity[split:p.max_moves]

        space.add(child.body, child.shape)
        offspring.append(child)

    p.population.clear()
    p.population = offspring


def mutation(p):
    chance = random.randint(0, 100)
    num_mutated = random.randint(0, p.size)

    if chance >= 100 - p.mutation_rate:
        p.mutation_happened = True
        for _ in range(num_mutated):
            mutated_arrow = p.population[random.randint(0, len(p.population) - 1)]
            for _ in range(50):
                x = random.randint(-50, 150)
                y = random.randint(-50, 150)

                mutated_arrow.angle[random.randint(0, p.max_moves - 1)] = random.uniform(-0.12, 0.12)
                mutated_arrow.velocity[random.randint(0, p.max_moves - 1)] = (x, y)
    else:
        p.mutation_happened = False
