import pygame
import window
import population as p


def main():
    screen = window.Screen()
    screen.setup()
    population = p.Population()
    population.create_population()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.exit()

        screen.screen.fill((0, 0, 0), (0, 0, screen.screen_width, screen.screen_height))
        screen.calc_fps(population)
        screen.draw_blocks(population)
        screen.draw_text(population)
        pygame.time.Clock().tick()
        pygame.display.flip()


if __name__ == "__main__":
    main()
