import pygame
from pytmx.util_pygame import load_pygame
# from PIL import Image

# 在窗口中显示图片
pygame.init()
screen = pygame.display.set_mode((256, 256))
tmx_data = load_pygame("worlds/1-1/W11.tmx")
layer_num = 0
# tileID_lst = []
for layer in tmx_data.visible_layers:
    for y in range(tmx_data.height):
        for x in range(tmx_data.width):

                # Getting pygame surface
            image = tmx_data.get_tile_image(x, y, layer_num)

                    # It's none if there are no tile in that place
            if image is not None:
                tileID = tmx_data.get_tile_gid(x, y, layer_num)
                # if tileID not in tileID_lst:
                    # tileID_lst.append(tileID)

                    # print(x, y, tileID)
                screen.blit(image, (0, 0))
                pygame.display.flip()
                img_name = 'temp_pic_full_xy_layernum_tileID/img' + '_' + str(x)+ '_' + str(y)+ '_' + str(layer_num)+ '_' + str(tileID)  + '.png'
                pygame.image.save(image,img_name)
                # while True:
                #     for event in pygame.event.get():
                #         if event.type == pygame.QUIT:
                #             pygame.quit()
                #             exit()
    layer_num += 1