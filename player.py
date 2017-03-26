import pygame
from pygame.locals import*
import os, sys
vec = pygame.math.Vector2
facingRight = True
gravity = 300000
friction = -3


class Character(pygame.sprite.Sprite):
    """ make main player character """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('cat_stand.png')
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()

        self.pos = vec(32, 576)
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)
        self.applyGravity = False

        self.animationFrames = 0  # counts the amount of frames a sprite has been displayed
        self.animationState = 0

    def update(self, dt):
        """ update the character """
        global facingRight

        self.updateAnimation()

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

        elif keys[pygame.K_UP]:
            if not self.applyGravity:
                self.vel.y = -350

        self.move(dt)

    def updateAnimation(self):
        """ walking animation"""
        walking = ['cat_walk_1.png', 'cat_walk_2.png', 'cat_walk_3.png',
                   'cat_walk_4.png']
        self.animationFrames = (self.animationFrames+1) % 10

        if self.animationFrames == 2:
            if int(self.vel.x) != 0:
                self.animationState = (self.animationState+1) % len(walking)
                image = pygame.image.load(walking[self.animationState])
                self.image = image.convert()
                self.image = image.convert_alpha()
            else:
                self.animationState = 0
                image = pygame.image.load('cat_stand.png')
                self.image = image.convert()
                self.image = image.convert_alpha()
            if not facingRight:
                self.image = pygame.transform.flip(self.image, True, False)


    def move(self, dt):
        """ handles character movement, physics calculations """
        # applying friction
        self.accel.x += self.vel.x * friction

        # Does gravity
        if self.applyGravity:
            self.accel = vec(self.accel.x, gravity*dt)
        else:
            self.accel = vec(self.accel.x, 0)
        # Movement Calculations
        self.pos += self.vel * dt + 0.5 * self.accel * (dt ** 2)
        self.vel += self.accel * dt

        # updates the position
        self.rect.midbottom = (self.pos)
