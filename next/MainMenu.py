import pygame as pg
import cv2
import sys


from Const import *
from Text import Text, Text_ch


class MainMenu(object):
    def __init__(self):
        self.mainImage = pg.image.load(r'images/super_mario_bros.png').convert_alpha()

        self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.735, WINDOW_H - WINDOW_H * 0.3))

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)

    def render_end(self, core):
        # core.screen.blit(pg.image.load(r'images/ending.png').convert_alpha(), (0,0))
        FPS = 25.5
        # FPSClock = pg.time.Clock()
        videoCapture = cv2.VideoCapture("images/opening.mp4")


        while True:
            # a=pg.time.get_ticks()
            if videoCapture.isOpened():
                #从opncv读一段视频进来
                ret, frame = videoCapture.read()
                #下面这句可以获取图像大小
                # print("frame.shape:", frame.shape)
                # 
                # rot90(m, k=1, axes=(0, 1)
                # m是要旋转的数组(矩阵)，
                # k是旋转的次数，默认旋转1次，
                # 那是顺时针还是逆时针呢？
                # 正数表示逆时针，而k为负数时则是对数组进行顺时针方向的旋转。
                # 视频结束时会丢出一个ValueError异常
                try:
                    # frame = np.rot90(frame,k=-1)
                    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                    # print(frame)
                except:
                    continue
                if frame is not None:

                    frame = pg.surfarray.make_surface(frame)

                    frame=pg.transform.flip(frame,False,True)
                    

                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
                    core.screen.blit(frame, (0,0))
            else:
                break
            for event in pg.event.get():  # 遍历所有事件
                if event.type == pg.QUIT:  # 如果单击关闭窗口，则退出
                    sys.exit()
            pg.display.flip()  # 更新全部显示
            # time_next= FPSClock.tick(FPS)
            # b=pg.time.get_ticks()
        videoCapture.release()
        cv2.destroyAllWindows()

 
 

# class EndMenu(object):
#     def __init__(self):
#         self.mainImage = pg.image.load('images/end_menu.png').convert_alpha()

#         # self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))

#     def render(self, core):
#         core.screen.blit(self.mainImage, (50, 50))
#         self.toStartText.render(core)
