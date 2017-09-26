import numpy as np

# Constants
DIM_X = 240
DIM_Y = 432
X_OFFSET = 0
Y_OFFSET = 37
MONITOR = {'top': Y_OFFSET, 'left': 0, 'width': DIM_X, 'height': DIM_Y}

MID_X = DIM_X / 2
MID_Y = DIM_Y / 2
DRAG_OFFSET = 30
DRAG_TIME = 0.20
CLICK_TIME = 0.1
PLAY_BUTTON_X = 150
PLAY_BUTTON_Y = 410 + Y_OFFSET
WAIT_SCREEN = 2.5

ROTATION_ANGLE = 15
BLOCK_X = 26
BLOCK_Y = 26
COLOR_LIST_FLOOR = np.array([
        [94, 216, 166], [87, 208, 160], # Grass
        [93, 78, 72], [48, 109, 84], # Grass
        [95, 255, 255], [0, 15, 255], # Coin
        [75, 74, 125], [57, 57, 113], [31, 30, 59], # Log
        [109, 185, 28], [87, 159, 15], [52, 75, 11], [83, 141, 21], # Lilypad
        [61, 59, 105], [92, 69, 71], [168, 131, 136], # Railroad
        ], np.int32)
