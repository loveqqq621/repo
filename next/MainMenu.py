import pygame as pg

from Const import *
from Text import Text, Text_ch


class MainMenu(object):
    def __init__(self):
        self.mainImage = pg.image.load(r'images/super_mario_bros.png').convert_alpha()

        self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)

    def render_end(self, core):
        core.screen.blit(pg.image.load('images/end_menu.png').convert_alpha(), (0, 0))
        # self.toStartText.render(core)
        Text_ch('测试 test', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3)).render(core)



# class EndMenu(object):
#     def __init__(self):
#         self.mainImage = pg.image.load('images/end_menu.png').convert_alpha()

#         # self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))

#     def render(self, core):
#         core.screen.blit(self.mainImage, (50, 50))
#         self.toStartText.render(core)
