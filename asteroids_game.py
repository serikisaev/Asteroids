import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

import common


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
    clock = pygame.time.Clock()
    objects = [ship]
    while True:
        dt = clock.tick(30) / 1000
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update(0.1)
        bullets.update()
        asteroids.update()
        screen.fill(ai_settings.bg_color)
        gf.update_screen(ai_settings, screen, ship, asteroids, bullets)
        ship.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
