import pygame
from pygame.locals import*
import ast
vec = pygame.math.Vector2
gravity = 30000


class Level():
    """
    Generic Level Class
    """
    def __init__(self, levelName):
        self.groundList = pygame.sprite.Group()
        self.fakeGroundList = pygame.sprite.Group()
        self.blockList = pygame.sprite.Group()
        self.deathList = pygame.sprite.Group()
        self.fallingObjectList = pygame.sprite.Group()
        self.spikesList = pygame.sprite.Group()
        self.windList = pygame.sprite.Group()
        self.levelMark = []

        self.screenShift = 0
        self.playerSpawn = vec(0, 0)

        f = open("levels/%s.txt" % levelName)

        text = "".join(f.read().split())  # get's rid of all whitespace

        f.close()

        playerStart = text.find('Player:')
        playerEnd = text.find('Ground:')
        groundStart = text.find('Ground:')
        groundEnd = text.find('Block:')
        blockStart = text.find('Block:')
        blockEnd = text.find('FallingObject:')
        fallingStart = text.find('FallingObject:')
        fallingEnd = text.find('Spikes:')
        spikesStart = text.find('Spikes:')
        spikesEnd = text.find('Wind:')
        windStart = text.find('Wind:')
        windEnd = text.find('Fake:')
        fakeStart = text.find('Fake:')
        fakeEnd = text.find('LevelMark:')
        levelMarkStart = text.find('LevelMark:')
        levelMarkEnd = len(text)+1

        playerSpawnList = ast.literal_eval(text[playerStart+7:playerEnd])
        groundPositions = ast.literal_eval(text[groundStart+7:groundEnd])
        blockPositions = ast.literal_eval(text[blockStart+6:blockEnd])
        fallingObjectPositions = ast.literal_eval(text[fallingStart+14:fallingEnd])
        spikesPositions = ast.literal_eval(text[spikesStart+7:spikesEnd])
        windPositions = ast.literal_eval(text[windStart+5:windEnd])
        fakeGroundPositions = ast.literal_eval(text[fakeStart+5:fakeEnd])
        levelMarkPosition = ast.literal_eval(text[levelMarkStart+10:levelMarkEnd])

        for position in groundPositions:
            ground = GroundBlock(position[0], position[1])
            self.groundList.add(ground)

        for position in fakeGroundPositions:
            fakeGround = fakeGroundBlock(position[0], position[1])
            self.fakeGroundList.add(fakeGround)

        for position in blockPositions:
            block = Block(position[0], position[1])
            self.blockList.add(block)

        for position in fallingObjectPositions:
            fallingObject = FallingObject(position[0], position[1])
            self.fallingObjectList.add(fallingObject)

        for position in spikesPositions:
            spikes = Spikes(position[0], position[1])
            self.spikesList.add(spikes)

        for position in windPositions:
            wind = Wind(position[0], position[1])
            self.windList.add(wind)

        for position in levelMarkPosition:
            self.levelMark  = LevelMark(levelMarkPosition[0][0],levelMarkPosition[0][1])

        self.allSprites = pygame.sprite.Group(self.blockList, self.deathList, self.groundList, self.fallingObjectList, self.windList, self.spikesList, self.levelMark)
        self.fakeGRoudSprites = pygame.sprite.Group(self.fakeGroundList)
        self.playerSpawn = vec(playerSpawnList[0], playerSpawnList[1])  # the initial position for the player

    def shiftScreen(self, shift_x):
        """ controls side scrolling of screen """


class GroundBlock(pygame.sprite.Sprite):
    """Level Ground"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/ground.png')

        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Block(pygame.sprite.Sprite):
    """ Level block elements for character to jump on """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/block.png')

        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y


class FallingObject(pygame.sprite.Sprite):
    """ Object that falls from ceiling kills character """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/death.png')
        self.gameheight = 1000
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.applyGravity = False
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)

    def trigger(self):
        self.applyGravity = True

    def update(self, dt, environmentSprites, deathElements):
        if self.applyGravity:
            self.accel = vec(0, gravity*dt)
        if pygame.sprite.spritecollideany(self, environmentSprites):
            self.accel.y = 0
            self.vel.y = 0

        self.rect.y += self.vel.y * dt + 0.5 * self.accel.y * (dt ** 2)
        # update velocity
        self.vel += self.accel * dt
        self.vel.x = int(self.vel.x)


class Wind(pygame.sprite.Sprite):
    """ Fan that propells character into ceiling, killing him """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/wind.png')
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.applyGravity = False
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)

    def update(self, dt, environmentSprites, deathElements):
        if self.applyGravity:
            self.accel = vec(0, gravity*dt)

        self.rect.y += self.vel.y * dt + 0.5 * self.accel.y * (dt ** 2)
        # update velocity
        self.vel += self.accel * dt
        self.vel.x = int(self.vel.x)

    def trigger(self):
        self.vel.y = -100


class Spikes(pygame.sprite.Sprite):
    """ spikes that pop up from ground and kill character """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/Spike.png')
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y


class LevelMark(pygame.sprite.Sprite):
    """When character touches an instance of this class, the next level is loaded"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/endlevelmark.png')
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
