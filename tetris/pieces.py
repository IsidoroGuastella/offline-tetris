
from tetris.constants import GRID_WIDTH

class Piece:
    def __init__(self, shape, color, x, y) -> None:
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    def clone(self):
        return Piece(self.shape, self.color, self.x, self.y)
    
    def reset_position(self):
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0
    
    def rotate(self):
        new_shape = list(zip(*reversed(self.shape)))
        return Piece(new_shape, self.color, self.x, self.y)