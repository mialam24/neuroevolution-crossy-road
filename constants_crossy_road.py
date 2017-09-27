import numpy as np

# Constants
NUM_GENERATIONS = 2
NUM_INDIVIDUALS = 3

DIM_X = 240
DIM_Y = 432
X_OFFSET = 0
Y_OFFSET = 37
MONITOR = {'top': Y_OFFSET, 'left': X_OFFSET, 
        'width': DIM_X, 'height': DIM_Y}

DIGIT_X = 4
DIGIT_Y = 5
DIGIT_WIDTH = 34
DIGIT_WIDTH_ONE = 21
DIGIT_HEIGHT = 33

PY_PAUSE = 0.0
MID_X = DIM_X / 2
MID_Y = DIM_Y / 2
PRESS_TIME = 0.05
MOVE_TIME = 0.25
PLAY_BUTTON_X = 150
PLAY_BUTTON_Y = 410 + Y_OFFSET
WAIT_SCREEN = 3
IDX_NOTHING = 0
IDX_UP = 1
IDX_DOWN = 2
IDX_LEFT = 3
IDX_RIGHT = 4

ROTATION_ANGLE = 15
BLOCK_X = 26
BLOCK_Y = 26
DEATH = -1
FLOOR = 0
CHICKEN = 1

COLOR_LIST_CHICKEN = np.array([
    [174, 139, 138], [139, 87, 85]], np.int32)

COLOR_LIST_FLOOR_SIMPLE = np.array([
        [94, 216, 166], [87, 208, 160], # Grass
        [93, 78, 72], [140, 118, 109], # Road
        [61, 59, 105], [92, 69, 71], [168, 131, 136], # Railroad
        ], np.int32)
        
COLOR_LIST_FLOOR_TRICKY = np.array([
        [95, 255, 255], # Coin
        [75, 74, 125], [57, 57, 113], # Log
        [109, 185, 28], [87, 159, 15], # Lilypad
        ], np.int32)

HOME_CELL_X = 9
HOME_CELL_Y = 13
GAME_OVER_COLOR = [249, 199, 86]
GREAT_X = 200
GREAT_Y = 150
GREAT_SCORE_COLOR = [236, 206, 105]
GAME_STATUS_GAME_OVER = -1
GAME_STATUS_GREAT_SCORE = 1
GAME_STATUS_PLAYING = 0

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


