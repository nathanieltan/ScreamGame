import pygame
from pygame.locals import *
import os, sys
from environment import *
from player import *
from voiceAmplitude import *
import threading
import queue
from dataProcessing import dataTrain

i = 0
clock = pygame.time.Clock()
dt = None
displayDebug = False  # variable that controls whether debug info is being displayed


class ScreamGameMain(threading.Thread):
    """This class defines the game itself. Includes game initialization and game loop"""
    def __init__(self, width=1856, height=768):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.recording = recordingThread()
        self.recording.start()

        self.gameState = 0  # 0 is playing game, 1 is death screen, 2 is win screen
        self.currentLevel = 1  # the level number

        self.characterDeaths = 0

    def run(self):
        self.MainLoop()

    def MainLoop(self):
        """ main loop of game """
        self.loadSprites(self.currentLevel)
        global displayDebug
        global dt
        # calibration()
        # allow player to hold down keys for continous input
        pygame.key.set_repeat(50, 100)

        self.background = pygame.image.load('images/clouds.jpg')
        self.background = self.background.convert()

        self.deathScreen = pygame.image.load('images/deathScreen.png')
        self.winScreen = pygame.image.load('images/winScreen.png')

        while 1:
            global i
            dtime_ms = clock.tick(60)  # gets the tick time in milliseconds
            dt = dtime_ms/1000  # converting the tick time to seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.recording.stop()
                    pygame.display.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    # toggle debugging screen
                    if keys[pygame.K_F3]:
                        if displayDebug:
                            displayDebug = False
                        else:
                            displayDebug = True

                    # resets the level after death
                    if keys[pygame.K_RETURN]:
                        i = 0
                        if self.gameState == 1:
                            self.gameState = 0
                            characterDeathsCopy = 0
                            for sprite in self.gameSprites.sprites():
                                sprite.kill()
                            self.loadSprites(self.currentLevel)
                            self.character.deaths = self.characterDeaths

            # Checks if character has reached the end of the level
            if pygame.sprite.spritecollideany(self.character, self.levelMark):
                i = 0
                for sprite in self.gameSprites.sprites():
                    sprite.kill()
                if self.currentLevel == 11:
                    self.gameState = 2
                else:
                    self.currentLevel = self.currentLevel+1
                    self.loadSprites(self.currentLevel)

            if self.gameState == 0:
                self.drawGame()
                self.update()
            elif self.gameState == 1:   # lose screen
                self.drawDeathScreen()
            elif self.gameState == 2:   # win screen
                self.drawWinScreen()

    def update(self):
        global dt

        # Trigger for falling objects
        global i

        self.characterDeaths = self.character.deaths

        deathObject = [death for death in self.triggerElements]
        deathObject.sort(key=lambda death: death.rect.x)

        # triggers death elements if recording thread passes trigger in queue
        if recordingQueue() == 'A':
            recordingQueue.get()
            if i <= len(deathObject) - 1:
                    deathObject[i].trigger()
                    i += 1
        if recordingQueue() == 'E':
            recordingQueue.get()
            time.sleep(2)
            if i <= len(deathObject) - 1:
                    deathObject[i].trigger()
                    i += 1
        if recordingQueue() == 'O':
            recordingQueue.get()
            time.sleep(5)
            if i <= len(deathObject) - 1:
                    deathObject[i].trigger()
                    i += 1

        # kills sprite if they go above game window
        for sprite in self.gameSprites.sprites():
            pass
            if sprite.rect.top > self.height:
                sprite.kill()

        # changes game state to lose
        if not self.character.alive():
            self.gameState = 1

        # calls the update function in all sprites
        self.gameSprites.update(dt,self.safeEnviron,self.deathElements)

    def drawGame(self):
        """Draws all sprites and text onto the screen and blits surfaces"""
        global amp
        self.screen.blit(self.background, (0, 0))
        self.gameSprites.draw(self.screen)

        if amplitudeQueue.empty():
            amp = 0.00
        else:
            amp = amplitudeQueue.get()

        # sets height to correspond to amplitude, displays amplitude
        height = -amp*1000
        if height < -80:
            height = -80
        pygame.draw.rect(self.screen, (255, 255, 255), (25, 35, 100, 110))
        pygame.draw.rect(self.screen, (0, 0, 255), (35, 120, 80, height))

        if pygame.font:
            font = pygame.font.Font(None, 24)
            text = font.render("Amplitude", 1, (0, 0, 0))
            textpos = text.get_rect(top=125, centerx=75)

            # displays character death count
            deathCountFont = pygame.font.Font(None, 24)
            deathCountText = font.render("Death Counter: %s"%self.character.deaths, 1, (128, 128, 128))
            deathCounterTextPos = text.get_rect(top=730, centerx=1750)

            pygame.draw.rect(self.screen, (0, 0, 0), (1700, 725, 150, 25))  # Rectangle behind death counter

            self.screen.blit(text, textpos)
            self.screen.blit(deathCountText,deathCounterTextPos)

        if displayDebug:
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("Gravity: %s Velocity: %s,%s" %
                                   (self.character.applyGravity,int(self.character.vel.x),int(self.character.vel.y)),1,(0,0,0))
                textpos = text.get_rect(top=100, centerx = self.screen.get_width()/2)
                self.screen.blit(text, textpos)

        pygame.display.flip()

    def drawDeathScreen(self):
        self.screen.blit(self.deathScreen,(0,0))
        pygame.display.flip()

    def drawWinScreen(self):
        self.screen.blit(self.winScreen,(0,0))
        pygame.display.flip()

    def loadSprites(self,level):
        self.lvl = Level("level%d" %(level))
        self.character = Character(self.lvl.playerSpawn)

        self.gameSprites = pygame.sprite.Group(self.character, self.lvl.groundList,
                                               self.lvl.blockList,self.lvl.fallingObjectList,self.lvl.windList,self.lvl.spikesList,self.lvl.levelMark)
        # Sprite Group for environment sprites that won't kill the character
        self.safeEnviron = pygame.sprite.Group(self.lvl.blockList, self.lvl.groundList)
        # Sprite Group for environment sprites that will kill the character
        self.deathElements = pygame.sprite.Group(self.lvl.fallingObjectList,self.lvl.windList,self.lvl.spikesList)
        # Sprite group for death elements that are triggered by voice
        self.triggerElements = pygame.sprite.Group(self.lvl.fallingObjectList,self.lvl.windList)

        self.levelMark = pygame.sprite.Group(self.lvl.levelMark)

if __name__ == "__main__":
    training_data = dataTrain(sound.txt)
    nn = nnet.Neural_Network(len(training_data[0][0]), 12, len(training_data[0][1]))
    MainWindow = ScreamGameMain()
    MainWindow.start()
