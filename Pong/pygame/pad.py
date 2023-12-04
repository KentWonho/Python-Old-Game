import pygame
import config


class Pad:
    def __init__(self, screen, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.screen = screen
        self.pad_rect = pygame.Rect(posx, posy, config.PAD_WIDTH, config.PAD_HEIGHT)
        self.pad_draw = pygame.draw.rect(screen, self.color, self.pad_rect)
        self.score = 0

    def display(self):
        self.pad_draw = pygame.draw.rect(self.screen, self.color, self.pad_rect)

    def update(self, y_fac):
        self.posy = self.posy + config.PAD_SPEED * y_fac

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + config.PAD_HEIGHT >= config.HEIGHT:
            self.posy = config.HEIGHT - config.PAD_HEIGHT

        self.pad_rect = pygame.Rect(self.posx, self.posy, config.PAD_WIDTH, config.PAD_HEIGHT)

    def goal(self):
        self.score += 1

    def display_score(self, text, x, y):
        DEFAULT_FONT = pygame.font.SysFont("airal", 30, False, False)
        text_draw = DEFAULT_FONT.render(f"{text} {self.score}", True, config.WHITE)
        text_rect = text_draw.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_draw, text_rect)

    def get_rect(self):
        return self.pad_rect

    def ball_collision(self, ball_rect):
        return pygame.Rect.colliderect(self.pad_rect, ball_rect)
