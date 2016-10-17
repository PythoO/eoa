import pygame
import config


class ScreenSwitch():

    def update(self, screen):
        config.x_animate += 5
        print config.x_animate
        if config.x_animate >= 640:
            config.x_animate = 0

        rect = pygame.rect.Rect((config.x_animate, 0, 2, 640))
        pygame.draw.rect(screen, (150, 0, 128), rect)
