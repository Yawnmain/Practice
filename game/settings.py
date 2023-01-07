import math

#_____Настройки_____
WIDTH = 1600
HEIGHT = 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 120
BLOCK = 50

#_____Настройки игрока_____
PLAYER_POS = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
PLAYER_ANGLE = 0
MOVEMENT_SPEED = 2

#_____Настройки карты_____
MAP_SCALE = 5

#_____Настройки рейкастинга_____
FOV = math.pi / 2.5
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 900
DELTA_ANGLE = FOV / NUM_RAYS
DISTANCE = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJECTION_COEFFICIENT = 3 * DISTANCE * BLOCK
FOV_SIZE = WIDTH // NUM_RAYS

#_____Настройки текстур_____
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // BLOCK

#_____Настройки спрайтов_____
DOUBLE_PI = math.pi * 2
CENTRALLY_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100

#_____Цвета_____
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (50, 50, 50)
LIGHTGRAY = (240, 240, 240)
SKY = (0, 186, 255)
FLOOR = (0, 101, 62)