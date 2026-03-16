
# Def of colors used in game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128) # Grid color

# Tetramino's shapes
SHAPES = [
    [[1,1,1,1]], # I-shape
    [[1,1],[1,1]], # O-shape
    [[1,1,1],[0,1,0]], # T-shape
    [[1,1,1],[1,0,0]], # L-shape
    [[1,1,1],[0,0,1]], # J-shape
    [[1,1,0],[0,1,1]], # S-shape
    [[0,1,1],[1,1,0]] # Z-shape
]

# Dim of game view
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
BORDER_WIDTH = 4
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH + BORDER_WIDTH * 2 + 200
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT + BORDER_WIDTH

# Colors avaible for Tetraminos
COLORS = [CYAN, YELLOW, MAGENTA, RED, GREEN, BLUE, ORANGE]

# FPS
FPS = 2000