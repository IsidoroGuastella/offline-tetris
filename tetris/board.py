
class Board:

    def __init__(self, GRID_WIDTH, GRID_HEIGHT) -> None:
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]


    def valid_move(self, piece, x, y) -> bool: 
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    if (x + j < 0 or x + j >= self.width or y + i >= self.height or (y + i >= 0 and self.grid[y + i][x + j])):
                        return False
        return True
    
    def place_piece(self, piece) -> None:
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[piece.y + i][piece.x + j] = piece.color
    
    def remove_full_rows(self) -> int:
        full_rows = [i for i, row in enumerate(self.grid) if all(row)]
        for row in full_rows:
            del self.grid[row]
            self.grid.insert(0, [0 for _ in range(self.width)])
        return len(full_rows)
