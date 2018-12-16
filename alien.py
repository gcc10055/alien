# -*- coding: UTF-8 -*-
import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """
        表示外星人的类
    """
    def __init__(self, ai_settings, screen):
        """
            初始化外星人并设置其初始化位置
        :param ai_settings:
        :param screen:
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像,并设置其rect属性
        self.image = pygame.image.load('images/alien1.png')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附近
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        self.rect.x = 0
        self.rect.y = 0

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """
        在指定的位置绘制外星人
        :return:
        """
        self.screen.blit(self.image, self.rect)
