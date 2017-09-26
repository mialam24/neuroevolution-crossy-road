import numpy as np

# Constants
DIM_X = 240
DIM_Y = 432
X_OFFSET = 0
Y_OFFSET = 37
MONITOR = {'top': Y_OFFSET, 'left': 0, 'width': DIM_X, 'height': DIM_Y}

MID_X = DIM_X / 2
MID_Y = DIM_Y / 2
PRESS_TIME = 0.01
MOVE_TIME = 0.25
PLAY_BUTTON_X = 150
PLAY_BUTTON_Y = 410 + Y_OFFSET
WAIT_SCREEN = 2.5
NOTHING = 0
UP = 1j
DOWN = -1j
LEFT = -1
RIGHT = 1

ROTATION_ANGLE = 15
BLOCK_X = 26
BLOCK_Y = 26
DEATH = -1
FLOOR = 0
COLOR_LIST_FLOOR = np.array([
        [94, 216, 166], [87, 208, 160], # Grass
        [93, 78, 72], [48, 109, 84], # Grass
        [95, 255, 255], [0, 15, 255], [54, 151, 171], [44, 105, 118], # Coin
        [75, 74, 125], [57, 57, 113], [31, 30, 59], [97, 101, 147], # Log
        [109, 185, 28], [87, 159, 15], [52, 75, 11], [83, 141, 21], # Lilypad
        [61, 59, 105], [92, 69, 71], [168, 131, 136], # Railroad
        ], np.int32)
HOME_CELL_X = 9
HOME_CELL_Y = 13
GAME_OVER_COLOR = [249, 199, 86]

IRRELEVANT_INPUT = [*range(0,8), *range(9, 16),
        *range(17,21), *range(26, 34), 
        34, *range(44,51), 
        51, *range(61,68), 
        68, *range(79,85), 
        102, 103, *range(113,119), 
        *range(119,122), *range(131,136), 
        *range(136,139), *range(149,153),
        *range(153,157), *range(166,170),
        *range(170,174), *range(184,187),
        *range(187,192), *range(201,204),
        *range(204,209), 219, 220,
        *range(221,227), 236, 237,
        *range(238,244), 254,
        *range(255,262), 271,
        *range(272,279), 288,
        *range(289,297), *range(301,306),
        *range(306,314), *range(315,323)]
