
import pygame
from tetris.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from tetris.game import Tetris
from tetris.menu import Menu
from tetris.users import User


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")

    profile = User.load()
    menu = Menu(screen, profile)

    while True:
        action = menu.run()

        if action == "play":
            game = Tetris(screen, profile)
            if game.run() == "quit":
                break

        elif action == "quit": break

    pygame.quit()
    
if __name__ == "__main__":
    main()