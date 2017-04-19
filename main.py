import pygame
from pygame.locals import *
import os, sys
from environment import *
from player import *
from voiceAmplitude import *
import threading
import queue

clock = pygame.time.Clock()
dt = None
displayDebug = False  # variable that controls whether debug info is being displayed


class ScreamGameMain(threading.Thread):
    def __init__(self, width=1000, height=1000):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.recording = recordingThread()
        self.recording.start()
    def run(self):
        self.MainLoop()

    def MainLoop(self):
        """ main loop of game """
        self.loadSprites()
        global displayDebug
        global dt
        # calibration()
        # allow player to hold down keys for continous input
        pygame.key.set_repeat(50, 100)

        self.background = pygame.image.load('images/clouds.jpg')
        self.background = self.background.convert()

        while 1:
            dtime_ms = clock.tick(60)  # gets the tick time in milliseconds
            dt = dtime_ms/1000  # converting the tick time to seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.recording.stop()
                    pygame.display.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_F3]:
                        if displayDebug:
                            displayDebug = False
                        else:
                            displayDebug = True
            #if check_Trigger():
            #    character.vel.y = -350
            #    character.applyGravity = True
            self.draw()
            self.update()

    def update(self):
        global dt

        if not recordingQueue.empty():
            if not self.character.applyGravity:
                self.character.vel.y = -350
                self.character.applyGravity = True
        self.gameSprites.update(dt,self.allEnviron,self.deathElements)

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
        self.lvl = Level("level2")
        self.character = Character(self.lvl.playerSpawn)

        self.gameSprites = pygame.sprite.Group(self.character, self.lvl.groundList,
                                               self.lvl.blockList,self.lvl.fallingObjectList)
        # Sprite Group for environment sprites that won't kill the character
        self.safeEnviron = pygame.sprite.Group(self.lvl.blockList, self.lvl.groundList)
        # Sprite Group for environment sprites that will kill the character
        self.deathElements = pygame.sprite.Group(self.lvl.fallingObjectList)
        # Sprite Group for all environment
        self.allEnviron = pygame.sprite.Group(self.lvl.blockList,self.lvl.groundList)


if __name__ == "__main__":
    MainWindow = ScreamGameMain()
    MainWindow.start()
