import pygame, math, random
from pygame.sprite import Sprite

class Asteroid(Sprite):
    def __init__(self, ai_settings, screen):
        super(Asteroid, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.original_image = pygame.image.load('images\large.bmp')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.radius = int(self.rect.width * .85 / 2)

        self.angle = random.randint(1, 360)
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.vx = random.randint(-1, 1)
        self.vy = random.randint(-1, 1)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)

        if self.rect.x < 0:
            self.rect.x = 840
        if self.rect.x > 840:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 840
        if self.rect.y > 840:
            self.rect.y = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)