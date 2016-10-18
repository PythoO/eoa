#!/usr/bin/python
# coding: utf8

"""
E.O.A : Extreme Operating Assistant.
"""
# Import module.
import sys
import pygame
from pygame.locals import *
import config

# Import sense.
from sense import voice

# UI import
from ui.core import UI
from ui.screen_switch import ScreenSwitch
from ui.forecast import Forecast
from ui.twitter import Twitter

# Import neuron.
import neuron.profile as profile

# Initialize screen.
size = width, height = 800, 600
pygame.init()
pygame.display.set_caption('E.O.A :: Extreme Operating Assistant')
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# voice.speech('System is loading.')

clock = pygame.time.Clock()

# Create some colors.
colors = {
    'black': [0, 0, 0],
    'white': (255, 255, 255),
    'blue_dark_t': (39, 64, 139, 50),
    'blue_t': (58, 95, 205, 50),
    'blue_light_t': (72, 118, 255, 50),
}

# Initialize variables.
profile.load_profile()
core_screen = UI(screen, profile, colors)
home_screen = ''
forecast_screen = Forecast(screen, colors)
twitter_screen = Twitter(screen, colors)
todo_screen = ''
map_screen = ''
sw = ScreenSwitch()

while 1:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    core_screen.background()
    core_screen.header()
    core_screen.left_col()
    core_screen.footer()
    core_screen.menu()
    core_screen.create_frame()
    core_screen.menu()

    for display_screen in config.screens:
        if config.screens[display_screen]:
            if display_screen == 'forecast':
                forecast_screen.draw()
            if display_screen == 'twitter':
                twitter_screen.draw()
            if display_screen == 'exit':
                sys.exit()

    pygame.display.flip()
