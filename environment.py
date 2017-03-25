import pygame
from pygame.locals import*
import os, sys

class Level():
    """
    Generic Level Class
    """
    def __init__(self):
        pass


class Level_1():
    """
    Design for Level 1
    """
    def __init__(self):
        pass


class GroundBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class Block(pygame.sprite.Sprite):
    """ Level block elements for character to jump on """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class DeathElement(pygame.sprite.Sprite):
    """ General class for elements that kill character """
    def __init__(self):
        pass


class FallingObject(DeathElement):
    """ Object that falls from ceiling kills character """
    def __init__(self):
        pass


class Fan(DeathElement):
    """ Fan that propells character into ceiling, killing him """
    def __init__(self):
        pass
