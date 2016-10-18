# coding: utf8

from neuron.twitter import read_tweet
import pygame
import re
from ui.text import Text


class Twitter:
    def __init__(self, screen, colors):
        self.screen = screen
        self.colors = colors
        self.display_info = pygame.display.Info()
        self.screen_width = self.display_info.current_w
        self.screen_height = self.display_info.current_h
        self.tweets = read_tweet()
        print 'read twiiter'

    def draw(self):
        x, y = 85, 85
        for tweet in self.tweets:
            if tweet.author.screen_name != 'CommitStrip_fr':
                self.set_bloc(tweet.author.screen_name, x, y, 'author')
                self.set_bloc(str(tweet.author.created_at), x + 200, y, 'author')
                self.set_bloc(re.sub(r"(?:\@|https?\://)\S+", "", tweet.text), x, y + 20, 'tweet')
                y += 70

    def set_bloc(self, text, x, y, type):
        """ Function to draw a twwet bloc. """
        if type == 'author':
            self.draw_bloc(x, y, 180, 10, text, 10)
        else:
            self.draw_bloc(x, y - 11, self.screen_width - (85 - 10), 50, text, 10)

    def draw_bloc(self, x, y, width, height, text, size):
        """ Draw all twwet bloc. """
        bloc = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(bloc, self.colors['blue_light_t'],
                         (0, 0, width, height), 0)
        pygame.draw.rect(bloc, self.colors['white'],
                         (0, 0, width, height), 1)
        Text(bloc, text, 0, 0, width, height, size)
        self.screen.blit(bloc, (x, y))
