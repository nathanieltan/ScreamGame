import pygame
from pygame.locals import*


class Level():
    """
    Generic Level Class
    """
    def __init__(self):
        self.groundList = pygame.sprite.Group()
        self.blockList = pygame.sprite.Group()
        self.deathList = pygame.sprite.Group()
        self.screenShift = 0

    def shiftScreen(self, shift_x):
        """ controls side scrolling of screen """


class GroundBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('block.png')

        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()


class Block(pygame.sprite.Sprite):
    """ Level block elements for character to jump on """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('block.png')

        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()


class FallingObject(pygame.sprite.Sprite):
    """ Object that falls from ceiling kills character """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class Fan(pygame.sprite.Sprite):
    """ Fan that propells character into ceiling, killing him """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class Spikes(pygame.sprite.Sprite):
    """ spikes that pop up from ground and kill character """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class Level_1(Level):
    """
    Design for Level 1
    """
    def __init__(self):
        Level.__init__(self)

        groundPositions = [[0, 576],
                           [64, 576],
                           [192, 576],
                           [256, 576]]
        blockPositions = [[256, 512]]
        # fallObjectsPositions = []
        # spikePositions = []
        # fanPositions = []

        for position in groundPositions:
            ground = GroundBlock()
            ground.rect.x = position[0]
            ground.rect.y = position[1]
            self.groundList.add(ground)

        for position in blockPositions:
            block = Block()
            block.rect.x = position[0]
            block.rect.y = position[1]
            self.blockList.add(block)

        # for position in fallObjectsPositions:
        #     fallObject = FallingObject()
        #     block.rect.x = position[0]
        #     block.rect.y = position[1]
        #     self.deathList.add(fallObject)
