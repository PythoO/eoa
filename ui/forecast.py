# coding: utf8

from neuron.forecast import forecast_currently
from sense.voice import speech
from text import Text
import pygame
import config


class Forecast:
    def __init__(self, screen, colors):
        self.screen = screen
        self.colors = colors
        self.display_info = pygame.display.Info()
        self.screen_width = self.display_info.current_w
        self.screen_height = self.display_info.current_h
        self.currently = currently = forecast_currently()

    def draw(self):
        self.draw_temp()
        self.draw_icon()
        self.draw_summary()
        self.draw_humidity()
        self.draw_wind_speed()
        self.draw_visibility()


        # Text(self.screen, 'visibility: ' + str(currently.visibility), 60, 115, 200, 10)

        # speech(currently.summary)
        # speech(str(currently.temperature) + ' celsius.')

    def draw_temp(self):
        """ Function to draw temperature frame. """
        text = str(self.currently.temperature) + u' ˚C'
        self.draw_bloc(275, 75, 180, 180, text, 30)

    def draw_icon(self):
        """ Function to draw the forecast icon. """
        text = str(self.currently.icon)
        self.draw_bloc(85, 75, 180, 180, text, 10)
        # Todo : make icons
        #ico = pygame.image.load('img/forecast.png').convert_alpha()
        #ico = pygame.transform.scale(ico, (180, 180))
        #self.screen.blit(ico, (85, 75))

    def draw_humidity(self):
        """ Function to draw the humidity. """
        text = str(self.currently.humidity) + " %"
        self.draw_bloc(465, 75, 180, 180, text, 10)

    def draw_wind_speed(self):
        """ Function to draw the wind speed. """
        text = str(self.currently.windSpeed) + " kph"
        self.draw_bloc(465, 260, 180, 180, text, 10)

    def draw_summary(self):
        """ Function to draw the summary. """
        text = str(self.currently.summary)
        self.draw_bloc(85, 260, 370, 180, text, 10)

    def draw_visibility(self):
        """ Function to draw the visibility. """
        text = str(self.currently.visibility) + " km"
        self.draw_bloc(85, 445, 180, 130, text, 10)

    def draw_bloc(self, x, y, width, height, text, size):
        bloc = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(bloc, self.colors['blue_light_t'],
                         (0, 0, width, height), 0)
        pygame.draw.rect(bloc, self.colors['white'],
                         (0, 0, width, height), 1)
        Text(bloc, text, 0, 0, width, height, size)
        self.screen.blit(bloc, (x, y))
