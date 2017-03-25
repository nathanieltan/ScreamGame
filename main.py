import pygame
from pygame.locals import *
import os, sys
from environment import *
from player import *
clock = pygame.time.Clock()


class ScreamGameMain():
    def __init__(self, width=1000, height=1000):
        self.width = width
        self.height = height
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        """ main loop of game """
        self.loadSprites()

        # allow player to hold down keys for continous input
        pygame.key.set_repeat(50, 100)

        self.background = pygame.image.load('background.png')
        self.background = self.background.convert()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
            self.draw()
            self.update()

    def update(self):
        self.gameSprites.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.gameSprites.draw(self.screen)

        pygame.display.flip()

    def loadSprites(self):
        self.character = Character()
        self.lvl = Level_1()

        self.gameSprites = (self.character, self.lvl.groundList,
                            self.lvl.blockList)
