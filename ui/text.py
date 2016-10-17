import pygame


class Text(object):
    def __init__(self, screen, text, xpos, ypos, width, height, size):
        small_text = pygame.font.Font("freesansbold.ttf", size)
        text_surf, text_rect = self.text_objects(text, small_text)
        text_rect.center = ((xpos + (width / 2)), (ypos + (height / 2)))
        screen.blit(text_surf, text_rect)

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, (255, 255, 255))
        return text_surface, text_surface.get_rect()
