"""
Class to create all Buttons.
"""
import pygame


class Button(object):
    def __init__(self, screen, profile, colors, dimension, text=None, action=None, icon=None):
        self.screen = screen
        self.profile = profile
        self.colors = colors
        self.x = dimension['x']
        self.y = dimension['y']
        self.width = dimension['width']
        self.height = dimension['height']
        self.text = text
        self.action = action
        self.icon = icon
        self.draw()

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        box_surface_polygon = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            # IN
            pygame.draw.polygon(box_surface_polygon, self.colors['blue_dark_t'], ((25, 0), (0, 25), (25, 50), (50, 25)))
            pygame.draw.polygon(box_surface_polygon, self.colors['white'], ((25, 0), (0, 25), (25, 50), (50, 25)), 1)
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            # OUT
            pygame.draw.polygon(box_surface_polygon, self.colors['blue_light_t'],
                                ((25, 0), (0, 25), (25, 50), (50, 25)))
            pygame.draw.polygon(box_surface_polygon, self.colors['blue_dark_t'],
                                ((25, 0), (0, 25), (25, 50), (50, 25)), 1)

        self.screen.blit(box_surface_polygon, (self.x, self.y))
        if self.icon:
            ico = pygame.image.load(self.icon).convert_alpha()
            ico = pygame.transform.scale(ico, (self.width / 2 + 5, self.width / 2 + 5))
            self.screen.blit(ico, (self.x + 12, self.y + 10))
