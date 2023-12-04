from pygame import Rect

import config
import pygame


class Key:
    def __init__(self, screen, char, x, y, font):
        self.character = char
        self.status = config.KEY_UNUSED # -1:Fail, 0:Unused, 1:Success
        self.screen = screen
        self.font = font
        self.key_rect = Rect(x, y, config.KEY_WIDTH, config.KEY_HEIGHT)

    def get_rect(self):
        return self.key_rect

    def get_character(self):
        return self.character

    def get_status(self):
        return self.status

    def draw_key(self):
        bg_color = config.WHITE
        if self.status == config.KEY_OCCUR:
            bg_color = config.GREEN
        elif self.status == config.KEY_WRONG:
            bg_color = config.RED
        pygame.draw.rect(self.screen, bg_color, self.key_rect)
        text = self.font.render(self.character, True, config.BLACK)
        text_rect = text.get_rect(center=(self.key_rect.x + config.KEY_WIDTH / 2, self.key_rect.y + config.KEY_HEIGHT / 2))
        self.screen.blit(text, text_rect)
        if self.status == config.KEY_WRONG:
            pygame.draw.line(self.screen, config.BLACK, (self.key_rect.x, self.key_rect.y), (self.key_rect.right, self.key_rect.bottom))
        elif self.status == config.KEY_OCCUR:
            pygame.draw.circle(self.screen, config.BLACK, self.key_rect.center, self.key_rect.height // 2, width=1)

    def set_status(self, status):
        self.status = status
        return self.status


