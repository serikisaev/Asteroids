import sys

import pygame
from bullet import Bullet
from asteroid import Asteroid

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """проверяет нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.rotate_right = True
    elif event.key == pygame.K_LEFT:
        ship.rotate_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """проверяет поднятие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.rotate_right = False
    elif event.key == pygame.K_LEFT:
        ship.rotate_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """обрабатывает нажатия клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, asteroids, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    asteroids.draw(screen)
    pygame.display.flip()


def create_pound(ai_settings, screen, asteroids):
    """создание нескольких астероидов"""
    for asteroid_number in range(6):
        asteroid = Asteroid(ai_settings, screen)
        asteroids.add(asteroid)
        print(asteroids)