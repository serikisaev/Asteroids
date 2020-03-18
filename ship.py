import math

import pygame

from settings import Settings
import base
import common
from vector import Vector


class Ship(base.Thing):
    WIDTH = 30
    HEIGHT = 20

    def __init__(self, ai_settings, screen):
        th_settings = Settings()
        """инициализирует корабль и задает начальную точку"""
        self.screen = screen
        self.ai_settings = ai_settings
        #загрузка изображения корабля
        self.original_image = pygame.image.load('images\ship.bmp')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #каждый новый корабль появляется в центре
        self.rect.centerx = (th_settings.screen_width / 2)
        self.rect.centery = (th_settings.screen_height / 2)
        self.angle = 13

        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.draw.aalines(self.surface, common.BLACK, True, ((0, 0), (self.WIDTH, self.HEIGHT / 2), (0, self.HEIGHT), (self.WIDTH * 0.1, self.HEIGHT / 2)))
        self.velocity = Vector(90, -20)
        self.position = Vector(400, 400)
        self.friction = 0.4
        self.mass = 10

    def draw(self, surface):
        rotated_surface = pygame.transform.rotate(self.surface, self.angle)
        rotated_surface.get_rect(center=self.surface.center)
        #rotated_surface.get_rect(center=self.surface.get_rect().center)
        #self.surface = rotated_surface.get_rect(center=self.surface.center)
        surface.blit(rotated_surface, self.position.values)
        #surface.blit(rotated_surface, new_surf.topleft)

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

    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)