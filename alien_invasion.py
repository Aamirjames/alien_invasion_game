import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    # overall class to manage the game asstes and behaviours
    def __init__(self):
        # Initialize the game, and create game resources(backgroud settings to run the game).
        pygame.init()
        self.settings = Settings()  # For using settings

        # to set a display window(fetched width and height from settings)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  # To display player spaceship

        # Set the background color(screen background).
        self.bg_color = (230, 230, 230)      # Almost black

    def run_game(self):
        # Start the main loop for the game.
        while True:
            # For listening to the events/actions by player(pressing a keyboard key or moving mouse)
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop(after changing the background color).
        self.screen.fill(self.settings.bg_color)  # Fetched from settings
        self.ship.blitme()  # To draw the spaceship at it current location

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance(object) and run the game
    ai = AlienInvasion()
    ai.run_game()
