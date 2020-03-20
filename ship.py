import math

import pygame

import base
import common
from vector import Vector


class Ship(base.Thing):
    WIDTH = 30
    HEIGHT = 20

    def __init__(self):

        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.draw.aalines(self.surface, common.BLACK, True, ((0, 0), (self.WIDTH, self.HEIGHT / 2), (0, self.HEIGHT), (self.WIDTH * 0.1, self.HEIGHT / 2)))
        self.velocity = Vector(90, -20)
        self.position = Vector(400, 400)
        self.friction = 0.4
        self.mass = 10
        self.angle = 50

    def draw(self, surface):
        rotated_surface = pygame.transform.rotate(self.surface, self.angle)
        new_surf = rotated_surface.get_rect(center=self.position.values)
        surface.blit(rotated_surface, new_surf.topleft)

    def apply_propulsion(self, propulsion):
        angle = math.radians(self.angle) + math.pi / 2
        self.velocity += Vector(propulsion * math.sin(angle), propulsion * math.cos(angle)) / self.mass

    def update(self, dt):
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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.angle -= 3
        elif keys[pygame.K_LEFT]:
            self.angle += 3
        elif keys[pygame.K_UP]:
            self.apply_propulsion(40)
        elif keys[pygame.K_DOWN]:
            self.apply_propulsion(-40)