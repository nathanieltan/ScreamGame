import pygame
from pygame.locals import *
import os, sys
from environment import *
from player import *
clock = pygame.time.Clock()
dt = None
displayDebug = False  # variable that controls whether debug info is being displayed

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
        global displayDebug
        global dt
        # allow player to hold down keys for continous input
        pygame.key.set_repeat(50, 100)

        self.background = pygame.image.load('images/clouds.jpg')
        self.background = self.background.convert()

        while 1:
            dtime_ms = clock.tick(60)  # gets the tick time in milliseconds
            dt = dtime_ms/1000  # converting the tick time to seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_F3]:
                        if displayDebug:
                            displayDebug = False
                        else:
                            displayDebug = True
            self.draw()
            self.update()

    def update(self):
        global dt

        self.gameSprites.update(dt,self.allEnviron)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.gameSprites.draw(self.screen)

        if displayDebug:
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("Gravity: %s Velocity: %s,%s" %
                                   (self.character.applyGravity,int(self.character.vel.x),int(self.character.vel.y)),1,(0,0,0))
                textpos = text.get_rect(top=100, centerx = self.screen.get_width()/2)
                self.screen.blit(text, textpos)
        pygame.display.flip()

    def loadSprites(self):
        self.lvl = Level("editorTest")
        self.character = Character(self.lvl.playerSpawn)

        self.gameSprites = pygame.sprite.Group(self.character, self.lvl.groundList,
                                               self.lvl.blockList)
        # Sprite Group for environment sprites that won't kill the character
        self.safeEnviron = pygame.sprite.Group(self.lvl.blockList, self.lvl.groundList)
        # Sprite Group for environment sprites that will kill the character

        # Sprite Group for all environment
        self.allEnviron = pygame.sprite.Group(self.lvl.blockList,self.lvl.groundList)

if __name__ == "__main__":
    MainWindow = ScreamGameMain()
    MainWindow.MainLoop()
