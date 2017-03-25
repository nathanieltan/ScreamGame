import pygame
from pygame.locals import*
import os, sys
vec = pygame.math.Vector2

class Character(pygame.sprite.Sprite):
    """ make main player character """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        """ update the character """
        pass

    def updateAnimation(self):
        """ walking animation"""
        pass

    def move(self):
        """ handles character movement, physics calculations """
        pass
