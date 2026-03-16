
import pygame
from random import randint
from tetris.constants import COLORS, GRID_HEIGHT, GRID_WIDTH, SHAPES, FPS
from tetris.board import Board
from tetris.pieces import Piece
from tetris.renderer import Renderer


class Tetris:
    def __init__(self,screen, profile) -> None:
        self.screen = screen
        self.profile = profile
        self.renderer = Renderer(self.screen)
        
        self.clock = pygame.time.Clock()

        self.board = Board(GRID_WIDTH, GRID_HEIGHT)

        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()

        self.game_over = False
        self.score = 0
        
        self.move_delay = 100
        self.last_move_time = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_DOWN: 0}

        self.hold_piece = None
        self.can_hold = True
    
    def new_piece(self):
        index = randint(0, len(SHAPES)-1)
        shape = SHAPES[index]
        color = COLORS[index]

        piece = Piece(shape, color, 0, 0)
        piece.reset_position()
        return piece
    
    def handle_continuous_movement(self) -> None:
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_LEFT] and current_time - self.last_move_time[pygame.K_LEFT] > self.move_delay:
            if self.board.valid_move(self.current_piece, self.current_piece.x - 1, self.current_piece.y):
                self.current_piece.x -= 1
                self.last_move_time[pygame.K_LEFT] = current_time

        if keys[pygame.K_RIGHT] and current_time - self.last_move_time[pygame.K_RIGHT] > self.move_delay:
            if self.board.valid_move(self.current_piece, self.current_piece.x + 1, self.current_piece.y):
                self.current_piece.x += 1
                self.last_move_time[pygame.K_RIGHT] = current_time

        if keys[pygame.K_DOWN] and current_time - self.last_move_time[pygame.K_DOWN] > self.move_delay:
            if self.board.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y + 1):
                self.current_piece.y += 1
                self.last_move_time[pygame.K_DOWN] = current_time
    
    def get_ghost_piece(self):
        ghost = self.current_piece.clone()
        while self.board.valid_move(ghost, ghost.x, ghost.y + 1):
            ghost.y += 1
        return ghost

    def hold_current_piece(self):
        if not self.can_hold: return
        if self.hold_piece is None:
            self.hold_piece = self.current_piece
            self.current_piece = self.next_piece
            self.next_piece = self.new_piece()
        else:
            self.current_piece, self.hold_piece = self.hold_piece, self.current_piece
            self.current_piece.reset_position()
        
        self.can_hold = False

    def run(self) -> None:
        fall_time = 0
        fall_speed = 0.5

        while not self.game_over:
            fall_time += self.clock.get_rawtime()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.profile.register_score(self.score)
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        rotated_piece = self.current_piece.rotate()
                        
                        if self.board.valid_move(rotated_piece, rotated_piece.x, rotated_piece.y):
                            self.current_piece = rotated_piece
                        
                        elif self.board.valid_move(rotated_piece, rotated_piece.x - 1, rotated_piece.y):
                            rotated_piece.x -= 1
                            self.current_piece = rotated_piece
                        
                        elif self.board.valid_move(rotated_piece, rotated_piece.x + 1, rotated_piece.y):
                            rotated_piece.x += 1
                            self.current_piece = rotated_piece
        
                    if event.key == pygame.K_SPACE:
                        while self.board.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y + 1):
                            self.current_piece.y += 1
                    
                    if event.key == pygame.K_c:
                        self.hold_current_piece()

            self.handle_continuous_movement()

            if fall_time / 1000 > fall_speed:
                if self.board.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y + 1):
                    self.current_piece.y += 1
                else:
                    self.board.place_piece(self.current_piece)
                    self.can_hold = True

                    rows_cleared = self.board.remove_full_rows()
                    self.score += rows_cleared * 100
                    
                    self.current_piece = self.next_piece
                    self.current_piece.reset_position()
                    self.next_piece = self.new_piece()
                    
                    if not self.board.valid_move(self.current_piece, self.current_piece.x, self.current_piece.y):
                        self.game_over = True

                fall_time = 0

            ghost = self.get_ghost_piece()

            self.renderer.render(
                self.board.grid,
                self.current_piece,
                ghost,
                self.hold_piece,
                self.next_piece,
                self.score,
                max(self.score, self.profile.best_score),
                self.game_over
            )

        self.profile.register_score(self.score)
        return "menu"
