import pygame
from pygame.locals import *
import os, sys
from environment import *
from player import *
clock = pygame.time.Clock()
dt = None


class ScreamGameMain():
    def __init__(self, width=640, height=640):
        self.width = width
        self.height = height
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        """ main loop of game """
        self.loadSprites()
        global dt
        # allow player to hold down keys for continous input
        pygame.key.set_repeat(50, 100)

        self.background = pygame.image.load('clouds.jpg')
        self.background = self.background.convert()

        while 1:
            dtime_ms = clock.tick(60)  # gets the tick time in milliseconds
            dt = dtime_ms/1000  # converting the tick time to seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
            self.draw()
            self.update()

    def update(self):
        global dt

        # self.character.applyGravity = True
        self.gameSprites.update(dt)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.gameSprites.draw(self.screen)

        pygame.display.flip()

    def loadSprites(self):
        self.character = Character()
        self.lvl = Level_1()

        self.gameSprites = pygame.sprite.Group(self.character, self.lvl.groundList,
                                               self.lvl.blockList)


if __name__ == "__main__":
    MainWindow = ScreamGameMain()
    MainWindow.MainLoop()
