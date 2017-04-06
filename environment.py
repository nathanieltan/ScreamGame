import pygame
from pygame.locals import*
import ast
vec = pygame.math.Vector2

class Level():
    """
    Generic Level Class
    """
    def __init__(self):
        self.groundList = pygame.sprite.Group()
        self.blockList = pygame.sprite.Group()
        self.deathList = pygame.sprite.Group()
        self.screenShift = 0
        self.playerSpawn = vec(0,0)

    def shiftScreen(self, shift_x):
        """ controls side scrolling of screen """

class GroundBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/block.png')

        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Block(pygame.sprite.Sprite):
    """ Level block elements for character to jump on """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/block.png')

        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y


class FallingObject(pygame.sprite.Sprite):
    """ Object that falls from ceiling kills character """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        pass


class Fan(pygame.sprite.Sprite):
    """ Fan that propells character into ceiling, killing him """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        pass


class Spikes(pygame.sprite.Sprite):
    """ spikes that pop up from ground and kill character """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        pass


class Level_1(Level):
    """
    Design for Level 1
    """
    def __init__(self):
        Level.__init__(self)
        f = open("levels/level1.txt")

        text = "".join(f.read().split())
        print(text)
        f.close()

        playerStart = text.find('Player:')
        playerEnd = text.find('Ground:')
        groundStart = text.find('Ground:')
        groundEnd = text.find('Block:')
        blockStart = text.find('Block:')
        blockEnd = len(text)

        playerSpawnList = ast.literal_eval(text[playerStart+7:playerEnd])
        groundPositions = ast.literal_eval(text[groundStart+7:groundEnd])
        blockPositions = ast.literal_eval(text[blockStart+6:blockEnd])

        # fallObjectsPositions = []
        # spikePositions = []
        # fanPositions = []

        for position in groundPositions:
            ground = GroundBlock(position[0],position[1])
            self.groundList.add(ground)

        for position in blockPositions:
            block = Block(position[0],position[1])
            self.blockList.add(block)
        self.playerSpawn = vec(playerSpawnList[0],playerSpawnList[1])  # the initial position for the player
        # for position in fallObjectsPositions:
        #     fallObject = FallingObject()
        #     block.rect.x = position[0]
        #     block.rect.y = position[1]
        #     self.deathList.add(fallObject)
