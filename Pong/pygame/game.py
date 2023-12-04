import pygame
import sys
from pad import Pad
from ball import Ball
from pygame.locals import *

import config

pygame.init()  # 초기화
main_screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), 1, 32)  # 메인 디스플레이를 설정한다
clock = pygame.time.Clock()  # 시간 설정

pad_blue = Pad(main_screen, 20, (config.HEIGHT - 100) // 2, config.BLUE)
pad_red = Pad(main_screen, config.WIDTH - 30, (config.HEIGHT - 100) // 2, config.RED)
ball = Ball(main_screen, config.WIDTH // 2, config.HEIGHT // 2, config.BALL_SPEED)

pad_blue_fac, pad_red_fac = 0, 0

while True:  # 아래의 코드를 무한 반복한다.
    main_screen.fill(config.BLACK)

    # Collision detction
    if pad_blue.ball_collision(ball.get_rect()) or pad_red.ball_collision(ball.get_rect()):
        ball.hit()

    if ball.get_rect().x <= 0:
        pad_red.goal()
        ball.reset()
    elif ball.get_rect().x >= config.WIDTH:
        pad_blue.goal()
        ball.reset()

    for event in pygame.event.get():  # 발생한 입력 event 목록의 event마다 검사
        if event.type == QUIT:  # event의 type이 QUIT에 해당할 경우
            pygame.quit()  # pygame을 종료한다
            sys.exit()  # 창을 닫는다
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pad_red_fac = -1
            if event.key == pygame.K_DOWN:
                pad_red_fac = 1
            if event.key == pygame.K_w:
                pad_blue_fac = -1
            if event.key == pygame.K_s:
                pad_blue_fac = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pad_red_fac = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                pad_blue_fac = 0

    pad_blue.update(pad_blue_fac)
    pad_red.update(pad_red_fac)
    ball.update()

    pad_blue.display()
    pad_red.display()
    ball.display()

    pad_blue.display_score("Blue : ", 100, 20)
    pad_red.display_score("Red : ", config.WIDTH - 100, 20)

    pygame.display.update()  # 화면을 업데이트한다
    clock.tick(config.FPS)  # 화면 표시 회수 설정만큼 루프의 간격을 둔다
