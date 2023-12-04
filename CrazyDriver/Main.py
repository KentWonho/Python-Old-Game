import os.path
import random
import sys

import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

pygame.display.set_caption("Crazy Driver")

IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png"))
IMG_ENEMY = pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png"))
moveSpeed = 5

screen = pygame.display.set_mode((500, 800))

h = IMG_ROAD.get_width() // 2
v = IMG_ROAD.get_height() - (IMG_PLAYER.get_height() // 2)

player = pygame.sprite.Sprite()
player.image = IMG_PLAYER
player.surf = pygame.Surface(IMG_PLAYER.get_size())
player.rect = player.surf.get_rect(center=(h, v))

hl = IMG_ENEMY.get_width() // 2
hr = IMG_ROAD.get_height() - (IMG_PLAYER.get_height() // 2)
h = random.randrange(hl, hr)
v = 0

enemy = pygame.sprite.Sprite()
enemy.image = IMG_ENEMY
enemy.surf = pygame.Surface(IMG_ENEMY.get_size())
enemy.rect = enemy.surf.get_rect(center=(h, v))


while True:
    screen.blit(IMG_ROAD, (0, 0))
    screen.blit(player.image, player.rect)
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player.rect.left > 0:
        player.rect.move_ip(-moveSpeed, 0)
        if player.rect.left < 0:
            player.rect.left = 0
    if keys[K_RIGHT]  and player.rect.right < IMG_ROAD.get_width():
        player.rect.move_ip(moveSpeed, 0)
        if player.rect.right > IMG_ROAD.get_width():
            player.rect.right =  IMG_ROAD.get_width()

    screen.blit(enemy.image, enemy.rect)
    enemy.rect.move_ip(0, moveSpeed)
    if enemy.rect.bottom > IMG_ROAD.get_height():
        hl = IMG_ENEMY.get_width() // 2
        hr = IMG_ROAD.get_height() - (IMG_PLAYER.get_height() // 2)
        h = random.randrange(hl, hr)
        v = 0
        enemy.rect = enemy.surf.get_rect(center=(h, v))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
