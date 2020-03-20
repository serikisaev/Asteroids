import math

import random

import pygame

import base
import common
from vector import Vector
from pygame.sprite import Sprite

class Asteroid(base.Thing):
    WIDTH = 101
    HEIGHT = 101

    def __init__(self):

        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        rand_x = random.randint(0, 50)
        rand_y = random.randint(0, 50)
        rand_x1 = random.randint(25, 100)
        rand_y1 = random.randint(0, 50)
        rand_x2 = random.randint(50, 100)
        rand_y2 = random.randint(50, 100)
        rand_x3 = random.randint(0, 50)
        rand_y3 = random.randint(50, 100)
        k = ((rand_x, rand_y), (rand_x1, rand_y1), (rand_x2, rand_y2), (rand_x3, rand_y3))
        pygame.draw.aalines(self.surface, common.BLACK, True, k)
        #pygame.draw.aalines(self.surface, common.BLACK, True, ((0, 0), (self.WIDTH, self.HEIGHT / 2), (0, self.HEIGHT), (self.WIDTH * 0.1, self.HEIGHT / 2)))
        self.velocity = Vector(90, -20)
        self.position = Vector(300, 400)
        self.friction = 0.4
        self.mass = 20
        self.angle = 50

    def draw(self, surface):
        surface.blit(self.surface, self.position.values)

    def update(self, dt):
        angle = math.radians(self.angle) + math.pi / 2
        self.velocity += Vector(40 * math.sin(angle), 10 * math.cos(angle)) / self.mass
        self.position += self.velocity * dt
        self.velocity -= self.velocity * (self.friction * dt)

        if self.position[0] < 0:
            self.position = Vector(840, self.position[1])
        if self.position[0] > 840:
            self.position = Vector(0, self.position[1])
        if self.position[1] < 0:
            self.position = Vector(self.position[0], 840)
        if self.position[1] > 840:
            self.position = Vector(self.position[0], 0)
