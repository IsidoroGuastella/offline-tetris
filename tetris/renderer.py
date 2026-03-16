
import pygame
from tetris.constants import (GRAY, BLACK, WHITE, 
                              SCREEN_HEIGHT, SCREEN_WIDTH, BORDER_WIDTH, BLOCK_SIZE,)

class Renderer:
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw_border(self) -> None:
        pygame.draw.rect(self.screen, 
                         GRAY, 
                         (0, 0, SCREEN_WIDTH - 200, SCREEN_HEIGHT), 
                         BORDER_WIDTH)
    
    def draw_grid(self, grid) -> None:
        for y, row in enumerate(grid):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(self.screen, color,
                                     (x * BLOCK_SIZE + BORDER_WIDTH,
                                      y * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1))
    
    def draw_piece(self, piece) -> None:
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen,piece.color,
                                     ((piece.x + j) * BLOCK_SIZE + BORDER_WIDTH,
                                      (piece.y + i) * BLOCK_SIZE,
                                       BLOCK_SIZE - 1, BLOCK_SIZE - 1 ))
                  
    def draw_ghost(self, ghost) -> None:
        if not ghost: return

        for i, row in enumerate(ghost.shape):
            for j, cell in enumerate(row):
                if cell: 
                    pygame.draw.rect(self.screen, GRAY,
                                     ((ghost.x + j) * BLOCK_SIZE + BORDER_WIDTH,
                                      (ghost.y + i) * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1 ), 1)    
    
    def draw_hold(self, hold) -> None:
        text = self.font.render("Hold:", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH - 190, 200))

        if not hold: return

        for i, row in enumerate(hold.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, hold.color,
                                      (SCREEN_WIDTH - 150 + j * BLOCK_SIZE,
                                       240 + i * BLOCK_SIZE,
                                       BLOCK_SIZE - 1, BLOCK_SIZE - 1 ))
    
    def draw_next_piece(self, next_piece) -> None:
        text = self.font.render("Next:", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH - 190, 60))

        if not next_piece: return

        for i, row in enumerate(next_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, next_piece.color, 
                                     (SCREEN_WIDTH - 150 + j * BLOCK_SIZE,
                                      100 + i * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1 ))

    def draw_score(self, score) -> None:
        score_text = self.font.render(f"Score: {score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH - 190, 10))

    def draw_best_score(self, best_score) -> None:
        best_text = self.font.render(f"Best: {best_score}", True, WHITE)
        self.screen.blit(best_text, (SCREEN_WIDTH - 190, 40))
    
    def draw_game_over(self) -> None:
        game_over_text = self.font.render("GAME OVER", True, WHITE)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2))

    def render(self, grid, piece, ghost, hold, next_piece, score, best_score, game_over) -> None:
        self.screen.fill(BLACK)

        self.draw_border()
        self.draw_grid(grid)
        self.draw_ghost(ghost)
        self.draw_piece(piece)
        self.draw_next_piece(next_piece)
        self.draw_hold(hold)
        self.draw_score(score)
        self.draw_best_score(best_score)

        
        if game_over: self.draw_game_over()

        pygame.display.flip()
