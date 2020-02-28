import pygame, math

from settings import Settings

class Ship():

    def __init__ (self, ai_settings, screen):
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
        self.angle = 0
        #флаг вращения
        self.rotate_right = False
        self.rotate_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        #th_settings = Settings()

        if self.angle > 360:
            self.angle = 0
        if self.angle < -360:
            self.angle = 0

        if self.rotate_right:
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center = self.rect.center)
            self.angle -= 1
        if self.rotate_left:
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center = self.rect.center)
            self.angle += 1

        if self.moving_up:
            self.rect.centerx -= 2.5 * math.cos(math.radians(-self.angle + 90))  # для езды вперед
            self.rect.centery -= 2.5 * math.sin(math.radians(-self.angle + 90))

        if self.moving_down:
            self.rect.centerx += 2.5 * math.cos(math.radians(-self.angle + 90))  # для езды назад
            self.rect.centery += + 2.5 * math.sin(math.radians(-self.angle + 90))

        if self.rect.centerx < 0:
            self.rect.centerx = 840
        if self.rect.centerx > 840:
            self.rect.centerx = 0
        if self.rect.centery < 0:
            self.rect.centery = 840
        if self.rect.centery > 840:
            self.rect.centery = 0


    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)