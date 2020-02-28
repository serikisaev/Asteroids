import pygame, math
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.angle = ship.angle

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color

    def update(self):
        self.rect.centerx -= 5 * math.cos(math.radians(-self.angle + 90))
        self.rect.centery -= 5 * math.sin(math.radians(-self.angle + 90))

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)