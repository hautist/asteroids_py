# this allows us to use code from pygame lib in this file
import pygame

# import everything from constants.py
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")

        for obj in drawable:
            obj.draw(screen)
        updateable.update(dt)

        pygame.display.flip()

        # limit framerate to 60 (and covert dt from ms to seconds)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
