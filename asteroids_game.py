import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Androids Vector')
    ship = Ship(ai_settings, screen)
    bullets = Group()
    asteroids1 = pygame.sprite.Group()
    asteroids2 = pygame.sprite.Group()
    gf.create_pound(ai_settings, screen, asteroids1)
    gf.create_pound(ai_settings, screen, asteroids2)
    running = True
    while running:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        asteroids1.update()
        gf.update_screen(ai_settings, screen, ship, asteroids1, bullets)
        asteroids2.update()
        if pygame.sprite.groupcollide(asteroids1, asteroids2, False, False):
            print('stolk')
        gf.update_screen(ai_settings, screen, ship, asteroids2, bullets)

run_game()