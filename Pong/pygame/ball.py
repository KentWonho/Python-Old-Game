import pygame
import config


class Ball:
    def __init__(self, screen, posx, posy, speed=config.BALL_SPEED):
        self.posx = posx
        self.posy = posy
        self.speed = speed
        self.xFac = 1
        self.yFac = -1
        self.screen = screen
        self.ball = pygame.draw.circle(self.screen, config.WHITE, (self.posx, self.posy), config.BALL_RADIUS)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(self.screen, config.WHITE, (self.posx, self.posy), config.BALL_RADIUS)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        if self.posy <= 0 or self.posy >= config.HEIGHT:
            self.yFac *= -1

        return [self.posx, self.posy]

    def reset(self):
        self.posx = config.WIDTH // 2
        self.posy = config.HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def get_rect(self):
        return self.ball
