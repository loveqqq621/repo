WINDOW_W = 800
WINDOW_H = 448
FPS = 100

# Player physics
GRAVITY = 0.08

# 左右键加速度
SPEED_INCREASE_RATE = 0.038

# 左右键减速度：如果没有按方向键，会减速
SPEED_DECREASE_RATE = 0.018
# SPEED_DECREASE_RATE = 0.038

# 正常跳跃系数
JUMP_POWER = 4.8

FALL_MULTIPLIER = 2.0

# 不长按空格，掉落速度 = gravity * low_jump_multiplier
LOW_JUMP_MULTIPLIER = 3.0

MAX_MOVE_SPEED = 2.0
MAX_FASTMOVE_SPEED = 3.0
MAX_FALL_SPEED = 5.5


# icons tiled id

# 黄色问号 - 出coin
QUESTION_ICON_ID = 229

# 砖块
BRICK_ID = 230

# 粉色问号 - 出蘑菇/戒指
QUESTION_SPECIAL_ID = 231

TMX_FILE = 'worlds/1-1/W11_ver112.tmx'