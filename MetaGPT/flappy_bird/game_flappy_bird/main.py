import pygame
from game import Game

def main():
    pygame.init()

    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    game = Game(screen, clock)
    game.run()

    pygame.quit()
    
if __name__ == "__main__":
    main()
