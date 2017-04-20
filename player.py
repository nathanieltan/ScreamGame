import pygame
from pygame.locals import*
import os, sys
vec = pygame.math.Vector2
facingRight = True
gravity = 30000
friction = -3


class Character(pygame.sprite.Sprite):
    """ make main player character """

    def __init__(self, spawnPos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/hambo_stand.png')
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()

        # initializes physics vectors
        self.pos = spawnPos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)
        self.applyGravity = False

        self.animationFrames = 0  # counts the amount of frames a sprite has been displayed
        self.animationState = 0

    def update(self, dt, environment):
        """ update the character """
        global facingRight

        self.updateAnimation()

        # character keyboard inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.accel.x = -500
            if facingRight:
                facingRight = False
                self.image = pygame.transform.flip(self.image, True, False)

        elif keys[pygame.K_RIGHT]:
            self.accel.x = 500
            if not facingRight:
                facingRight = True
                self.image = pygame.transform.flip(self.image, True, False)
        elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.accel.x = 0

        if keys[pygame.K_UP] and not self.applyGravity:  # jumping
            self.vel.y = -350
            self.applyGravity = True

        # self.applyGravity = True

        # Does gravity
        if self.applyGravity:
            self.accel = vec(self.accel.x, gravity*dt)
        else:
            self.accel = vec(self.accel.x, 0)

        # x direction of movement
        self.accel.x += self.vel.x * friction  # applying friction
        self.pos.x += self.vel.x * dt + 0.5 * self.accel.x * (dt ** 2)
        self.rect.midbottom = (self.pos)
        self.collide(environment, self.vel.x, 0)

        # y direction of movement
        self.pos.y += self.vel.y * dt + 0.5 * self.accel.y * (dt ** 2)

        self.rect.midbottom = (self.pos)
        self.collide(environment, 0, self.vel.y)

        # update velocity
        self.vel += self.accel * dt
        self.vel.x = int(self.vel.x)

    def updateAnimation(self):
        """ walking animation"""
        # list of walking animation sprites
        walking = ['images/hambo_walk_1.png', 'images/hambo_walk_2.png']
        self.animationFrames = (self.animationFrames+1) % 10

        if self.animationFrames == 2:
            if int(self.vel.x) != 0:  # if the character is moving, moves along in the animation
                self.animationState = (self.animationState+1) % len(walking)
                image = pygame.image.load(walking[self.animationState])
                self.image = image.convert()
                self.image = image.convert_alpha()
            else:  # if the character isn't moving, changes sprite to the standing image
                self.animationState = 0
                image = pygame.image.load('images/hambo_stand.png')
                self.image = image.convert()
                self.image = image.convert_alpha()
            if not facingRight:  # makes sure the sprite is facing the correct direction
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale2x(self.image)

    def collide(self, environment, xvel, yvel):
        verticallyCollide = False
        for element in environment.sprites():
            if element.rect.colliderect(self.rect):
                if xvel > 0:
                    self.rect.right = element.rect.left
                if xvel < 0:
                    self.rect.left = element.rect.right
                if yvel > 0:
                    self.rect.midbottom = (self.pos.x, element.rect.top)
                    self.applyGravity = False
                    self.vel.y = 0
                if yvel < 0:
                    self.rect.top = element.rect.bottom
                self.pos.x = self.rect.midbottom[0]
                self.pos.y = self.rect.midbottom[1]
                verticallyCollide = True
        if not verticallyCollide:
            self.applyGravity = True

    def death():
        pass
