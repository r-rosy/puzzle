import pygame,sys

class Settings:
    def __init__(self):
        # 界面尺寸
        self.step = None
        self.display_height = 650
        self.display_width = 750

        # 字体大小
        self.SIZE = 20
        # 关卡阶数
        self.rank = 3
        # 时钟帧率
        self.clock = pygame.time.Clock()

        # 主矩形参数
        self.rect_x = 180
        self.rect_y = 180
        self.rect_width = 350
        self.rect_height = 350


        # 标记点个数
        self.MINECOUNT = 5

        # 计时器
        self.timer = 20
        self.step = 0

        # 错误机会
        self.Opportunity = 3


