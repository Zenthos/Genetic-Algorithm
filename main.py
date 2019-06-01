import pygame
import window
import popul


def main():
    frame = window.Frame()
    p = popul.Population()
    frame.space.add(p.target_body, p.target_shape)
    p.create_population(frame.screen, frame.space)
    while frame.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frame.exit()

        if p.lifespan == 1000:
            frame.shapes_finished.clear()
            p.lifespan = 0
            p.perform_ga(frame.screen, frame.space)
        else:
            p.lifespan += 1

        for arrow in p.population:
            arrow.move(p)

        frame.draw(p)
        frame.clock.tick(120)
        frame.space.step(1 / 60.0)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
