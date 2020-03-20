import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from asteroid import Asteroid
import game_functions as gf



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Androids Vector')
    ship = Ship()
    asteroid = Asteroid()
    bullets = Group()
    asteroids = pygame.sprite.Group()
    running = True
    clock = pygame.time.Clock()
    #objects = [ship]
    while True:
        dt = clock.tick(30) / 1000
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update(0.1)
        asteroid.update(0.1)
        bullets.update()
        screen.fill(ai_settings.bg_color)
        #gf.update_screen(ai_settings, screen, ship, asteroids, bullets)
        ship.draw(screen)
        asteroid.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
