import pygame
import random
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen, game_settings):
        super(Food, self).__init__()
        self.screen = screen
        # 加载苹果的图像
        self.image = pygame.image.load_basic('./images/ship.bmp')
        self.rect = self.image.get_rect()
        # 随机放置苹果
        self.rect.x = random.randint(0, game_settings.screen_width)
        self.rect.y = random.randint(0, game_settings.screen_height)

    def draw(self):
        self.screen.blit(self.image, self.rect)