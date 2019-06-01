import pygame
import pymunk
import pymunk.pygame_util


def add_ball(space, screen, position):
    mass = 1
    radius = 20
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = pymunk.pygame_util.from_pygame(position, screen)
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.filter = pymunk.ShapeFilter(categories=0b100, mask=pymunk.ShapeFilter.ALL_MASKS ^ 0b100)
    space.add(body, shape)
    return shape


def main():
    space = pymunk.Space()
    space.gravity = (0, -1000)
    screen = pygame.display.set_mode((800, 600))
    running = True
    b = []

    vertices = [(0, 0), (800, 0), (800, 50), (0, 50)]
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pymunk.pygame_util.from_pygame((0, 600), screen)
    shape = pymunk.Poly(body, vertices)
    shape.elasticity = 0.95
    space.add(body, shape)
    floor_shape = shape

    flr = pymunk.pygame_util.to_pygame(floor_shape.body.position, screen)
    rect = flr[0], flr[1] - 49, 800, 50

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                ball = add_ball(space, screen, pygame.mouse.get_pos())
                b.append(ball)

        screen.fill((26, 26, 29))
        pygame.draw.rect(screen, (31, 40, 53), rect, 0)

        for ball in b:
            p = pymunk.pygame_util.to_pygame(ball.body.position, screen)
            pygame.draw.circle(screen, (197, 198, 199), p, int(ball.radius), 0)

        space.step(1 / 50.0)
        pygame.time.Clock().tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
