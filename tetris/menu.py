
import pygame
from tetris.constants import SCREEN_WIDTH, BLACK, WHITE

class Menu:

    def __init__(self, screen, profile) -> None:
        self.screen = screen
        self.profile = profile
        self.font_big = pygame.font.Font(None, 72)
        self.font = pygame.font.Font(None,40)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.screen.fill(BLACK)

            title = self.font_big.render("TETRIS",True, WHITE)
            author = self.font.render("di Isidoro Guastella", True, WHITE)
            play = self.font.render("Press ENTER to play", True, WHITE)
            quit_text = self.font.render("Press ESC to quit", True, WHITE)
            player = self.font.render(f"Player: {self.profile.name}", True, WHITE)
            best = self.font.render(f"Best score: {self.profile.best_score}", True, WHITE)

            self.screen.blit(title, (SCREEN_WIDTH // 2 - 140, 150))
            self.screen.blit(author, (SCREEN_WIDTH // 2 - 140, 200))
            self.screen.blit(play, (SCREEN_WIDTH // 2 - 140, 300))
            self.screen.blit(quit_text, (SCREEN_WIDTH // 2 - 140, 350))
            self.screen.blit(player, (SCREEN_WIDTH // 2 - 140, 420))
            self.screen.blit(best, (SCREEN_WIDTH // 2 - 140, 460))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: return "quit"
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: return "play"
                    
                    if event.key == pygame.K_ESCAPE: return "quit"
