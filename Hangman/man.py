import pygame
import config


class Man:  # 단두대, 남자의 그림 까지
    def __init__(self, screen, width=config.WIDTH // 2, height=config.HEIGHT):
        self.width = width
        self.height = height
        self.life = config.LIFE
        self.screen = screen
        self.board_rect = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(screen, config.BOARD_COLOR, self.board_rect)
        # 단두대
        pygame.draw.line(screen, config.WHITE, (95, 530), (430, 530))
        pygame.draw.line(screen, config.WHITE, (142, 160), (142, 530))
        pygame.draw.line(screen, config.WHITE, (142, 160), (275, 160))
        pygame.draw.line(screen, config.WHITE, (275, 160), (275, 210))

        # 표정

    def lost_life(self):
        self.life = self.life - 1

        if self.life == 4:
            # 머리, 몸
            pygame.draw.circle(self.screen, config.WHITE, (275, 235), 25, width=1)
            pygame.draw.line(self.screen, config.WHITE, (275, 260), (275, 330))
        elif self.life == 3:
            # 왼팔
            pygame.draw.line(self.screen, config.WHITE, (275, 275), (235, 320))
        elif self.life == 2:
            # 오른팔
            pygame.draw.line(self.screen, config.WHITE, (275, 275), (315, 320))
        elif self.life == 1:
            # 왼다리
            pygame.draw.line(self.screen, config.WHITE, (275, 330), (235, 390))
        elif self.life == 0:
            # 오른다리
            pygame.draw.line(self.screen, config.WHITE, (275, 330), (315, 390))


    def get_life(self):
        return self.life
