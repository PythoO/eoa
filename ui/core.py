"""
The main UI.
"""
import pygame
from button import Button
import config
import datetime
from text import Text


class UI:
    blue_t = (95, 177, 255)

    def __init__(self, screen, profile, colors):
        self.screen = screen
        self.profile = profile
        self.colors = colors
        self.display_info = pygame.display.Info()
        self.screen_width = self.display_info.current_w
        self.screen_height = self.display_info.current_h

    def background(self):
        bg = pygame.image.load('bg.jpg').convert()
        self.screen.blit(bg, [0, 0])

    def header(self):
        header_surf = pygame.Surface((self.screen_width, 51), pygame.SRCALPHA)
        pygame.draw.polygon(header_surf, self.colors['blue_t'], ([0, 0], [50, 50], [self.screen_width - 20, 50], [
            self.screen_width, 0]), 0)
        pygame.draw.lines(header_surf, self.colors['blue_dark_t'], False,
                          ([0, 0], [50, 50], [self.screen_width - 20, 50], [
                              self.screen_width, 0]), 1)
        self.screen.blit(header_surf, (0, 0))

    def left_col(self):
        left_col_surf = pygame.Surface((71, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(left_col_surf, self.colors['blue_t'], ([0, 0], [70, 70], [70, self.screen_height - 20], [
            0, self.screen_height]), 0)
        pygame.draw.lines(left_col_surf, self.colors['blue_dark_t'], False,
                          ([0, 0], [70, 70], [70, self.screen_height - 20], [
                              0, self.screen_height]), 1)
        self.screen.blit(left_col_surf, (0, 0))

    def footer(self):
        footer_surf = pygame.Surface((200, 25), pygame.SRCALPHA)
        pygame.draw.polygon(footer_surf, self.colors['blue_t'], ([0, 25],
                                                                 [25, 0],
                                                                 [100, 0],
                                                                 [100, 25]), 0)
        pygame.draw.lines(footer_surf, self.colors['blue_dark_t'], False,
                          ([0, 25], [25, 0], [100, 0], [100, 25]), 1)

    def menu(self):
        # date.
        new_date = datetime.datetime.now().strftime("%d.%m.%y.%H:%M:%S")
        Text(self.screen, new_date, self.screen_width -110, 35, 100, 50, 10)
        # Forecast
        Button(self.screen, self.profile, self.colors, {'x': 10, 'y': 60, 'width': 50, 'height': 50}, None,
               self.get_forecast, 'img/cloud.png')
        # Exit
        Button(self.screen, self.profile, self.colors, {'x': self.screen_width - 55, 'y': 0, 'width': 50, 'height': 50}, None,
               self.get_exit, 'img/exit.png')

    def create_frame(self):
        # main frame
        frame_width = self.screen_width - 100
        frame_height = self.screen_height - 90
        frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
        pygame.draw.rect(frame, self.colors['blue_light_t'],
                         (0, 0, frame_width, frame_height), 0)
        pygame.draw.rect(frame, self.colors['white'],
                         (0, 0, frame_width, frame_height), 1)
        self.screen.blit(frame, (80, 70))

    def get_forecast(self):
        self.reset_screens()
        config.screens['forecast'] = True
        print config.screens

    def get_exit(self):
        self.reset_screens()
        config.screens['exit'] = True

    def reset_screens(self):
        for screen in config.screens:
            print screen
            config.screens[screen] = False
