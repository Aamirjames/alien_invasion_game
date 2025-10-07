import sys
import pygame


class AlienInvasion:
    # overall class to manage the game asstes and behaviours
    def __init__(self):
        # Initialize the game, and create game resources(bacgroud settings to run the game).
        pygame.init()

        # to set a display window
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # Start the main loop for the game.
        while True:
            # for listening to the events/actions by player(pressing a keyboard key or moving mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance(object) and run the game
    ai = AlienInvasion()
    ai.run_game()
