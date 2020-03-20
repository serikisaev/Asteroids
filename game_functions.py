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



