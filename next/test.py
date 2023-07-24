from moviepy.editor import *
import pygame
import ffmpeg

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('images/opening.mp4')
clip.preview()

pygame.quit()