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
    asteroids = pygame.sprite.Group()
    gf.create_pound(ai_settings, screen, asteroids)
    running = True
    while running:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        asteroids.update()
        gf.update_screen(ai_settings, screen, ship, asteroids, bullets)

run_game()