import pygame
from game import Game

def main():
    # Initialize the game engine
    pygame.init()

    # Define the game screen size
    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512

    # Create the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the game clock
    clock = pygame.time.Clock()

    # Create a new game instance
    game = Game(screen, clock)

    # Start the game loop
    while game.running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.bird.velocity = -10

        # Update the game state
        game.update()

        # Draw the game screen
        game.draw()

        # Tick the game clock
        clock.tick(60)

    # Quit the game
    pygame.quit()

if __name__ == "__main__":
    main()

