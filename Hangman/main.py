import re
import sys
import random

import pygame
from pygame.locals import QUIT

import config
from man import Man
from key import Key

pygame.init()

clock = None
main_screen = None
man = None
keyboard_list = None
status_rect = None
word_display_list = None
reset_bg_rect = None
game_end = None
DEFAULT_FONT = pygame.font.Font(None, 30)
DISPLAY_FONT = pygame.font.Font(None, 50)
OVER_FONT = pygame.font.Font(None, 120)
WORD_LIST = ["ANIMAL", "CARMEL", "DOG", "CAT", "RABBIT", "MOUSE", "TIGER", "BEAR", "COW", "DONKEY", "HORSE", "MONKEY"]
TARGET_WORD = ""


def get_life_text():
    global man
    life = "Life:"
    for i in range(man.get_life()):
        life += "O "
    return life


def init_keyboard():
    global main_screen
    global keyboard_list
    keyboard_area = pygame.Rect(config.WIDTH // 2, config.HEIGHT - config.KEYBOARD_AREA_HEIGHT,
                                config.WIDTH // 2, config.KEYBOARD_AREA_HEIGHT)
    keyboard_list = list(range(26))
    y = keyboard_area.y
    for i in range(len(keyboard_list)):
        if i % 13 == 0:
            x = keyboard_area.x
            y += config.KEY_HEIGHT
        else:
            x += config.KEY_WIDTH
        keyboard_list[i] = Key(main_screen, chr(ord('A') + i), x, y, pygame.font.Font(None, 30))
        keyboard_list[i].draw_key()


def init_life():
    global main_screen
    global status_rect
    life = DEFAULT_FONT.render(get_life_text(), True, config.WHITE)
    main_screen.blit(life, [config.WIDTH // 2 + 10, 10])
    status_rect = life.get_rect()
    status_rect.x = config.WIDTH // 2 + 10
    status_rect.y = 10


def init_display():
    global main_screen
    global word_display_list

    word_display_list = bytearray(len(TARGET_WORD))
    for i in range(len(word_display_list)):
        word_display_list[i] = ord("_")

    text = ""
    for i in range(len(word_display_list)):
        text += chr(word_display_list[i]) + "  "

    display = DISPLAY_FONT.render(text.lstrip(), True, config.WHITE)
    centery = ((config.WIDTH // 2 + 10) + config.WIDTH) // 2
    display_rect = display.get_rect(center=(centery, 286))
    main_screen.blit(display, display_rect)


def init():
    global clock
    global main_screen
    global man
    global TARGET_WORD

    main_screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), 1, 32)  # 메인 디스플레이를 설정한다
    clock = pygame.time.Clock()  # 시간 설정
    main_screen.fill(config.BLACK)
    man = Man(main_screen)

    TARGET_WORD = WORD_LIST[random.randint(0, len(WORD_LIST) - 1)]

    init_keyboard()
    init_life()
    init_display()
    pygame.display.update()


def check_character(ch):
    global TARGET_WORD
    global word_display_list
    ret = []
    for a in re.finditer(ch, TARGET_WORD):
        ret.append(a.start())
        word_display_list[a.start()] = ord(ch)
    return ret


def display_update():
    pygame.draw.rect(main_screen, config.BLACK, pygame.Rect(config.WIDTH // 2, 256, config.WIDTH // 2, 60))
    text = ""
    for i in range(len(word_display_list)):
        text += chr(word_display_list[i]) + "  "
    display = DISPLAY_FONT.render(text.lstrip(), True, config.WHITE)
    centery = ((config.WIDTH // 2 + 10) + config.WIDTH) // 2
    display_rect = display.get_rect(center=(centery, 286))
    main_screen.blit(display, display_rect)


def update_life():
    global main_screen
    global man
    global status_rect
    pygame.draw.rect(main_screen, config.BLACK, status_rect)
    life_render = DEFAULT_FONT.render(get_life_text(), True, config.WHITE)
    main_screen.blit(life_render, [config.WIDTH // 2 + 10, 10])


def key_click(x, y):
    global keyboard_list
    global man
    for key in keyboard_list:
        if key.get_rect().collidepoint(x, y) and key.get_status() == config.KEY_UNUSED:
            ret = check_character(key.get_character())
            if len(ret) > 0:
                key.set_status(config.KEY_OCCUR)
                display_update()
            else:
                key.set_status(config.KEY_WRONG)
                man.lost_life()

            key.draw_key()
            update_life()


def game_fail():
    global reset_bg_rect
    global game_end
    text = OVER_FONT.render("Fail. He is Die", True, config.RED)
    text = pygame.transform.rotate(text, 30)
    text_rect = text.get_rect(center=[config.WIDTH//2, config.HEIGHT//2])
    main_screen.blit(text, text_rect)

    reset_text = DISPLAY_FONT.render("RESET", True, config.WHITE)
    reset_bg_rect = reset_text.get_rect(right=config.WIDTH - 10, top=10)
    main_screen.blit(reset_text, reset_bg_rect)
    game_end = True


def game_success():
    global reset_bg_rect
    global game_end
    text = OVER_FONT.render("Success!", True, config.GREEN)
    text = pygame.transform.rotate(text, 30)
    text_rect = text.get_rect(center=[config.WIDTH//2, config.HEIGHT//2])
    main_screen.blit(text, text_rect)

    reset_text = DISPLAY_FONT.render("RESET", True, config.WHITE)
    reset_bg_rect = reset_text.get_rect(right=config.WIDTH - 10, top=10)
    main_screen.blit(reset_text, reset_bg_rect)
    game_end = True


def play():
    global man
    global game_end
    while True:  # 아래의 코드를 무한 반복한다.
        for event in pygame.event.get():  # 발생한 입력 event 목록의 event마다 검사
            if event.type == QUIT:  # event의 type이 QUIT에 해당할 경우
                pygame.quit()  # pygame을 종료한다
                sys.exit()  # 창을 닫는다
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game_end and reset_bg_rect.collidepoint(event.pos[0], event.pos[1]) :
                    init()
                else:
                    key_click(event.pos[0], event.pos[1])

        if man.get_life() <= 0:
            game_fail()
        elif word_display_list.find(b"_") < 0:
            game_success()

        pygame.display.update()
        clock.tick(config.FPS)  # 화면 표시 회수 설정만큼 루프의 간격을 둔다


if __name__ == "__main__":
    init()
    play()
