# this allows us to use code from pygame lib in this file
import pygame

# import everything from constants.py
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")
        pygame.display.flip()

        # limit framerate to 60 (and covert dt from ms to seconds)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
