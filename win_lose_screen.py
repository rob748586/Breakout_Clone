import pygame

from game_state import GameStateBase


class WinLoseScreen(GameStateBase):
    """ The win/lose screen game state displays the message passed to it in initialisation and waits for a key press"""
    def __init__(self, game, message):
        """ Initialise the object """
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.state_manager = game.state_manager
        self.message = message

    def on_create(self):
        """ Create the images for the message and prompt to press any key. """
        self.text = pygame.font.SysFont(None, 48).render(f"{self.message}", True, self.settings.text_colour)

        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = self.screen.get_rect().width / 2
        self.text_rect.centery = self.screen.get_rect().height / 2 - 10

        self.subtitle = pygame.font.SysFont(None, 24).render("Press any key to continue...", True,
                                                             self.settings.text_colour)
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.centerx = self.screen.get_rect().width / 2
        self.subtitle_rect.centery = self.screen.get_rect().height / 2 + 20

    def on_destroy(self):
        pass

    def do_updates(self, timeslice):
        pass

    def render(self):
        """ Render the message and press any key prompt. """
        pygame.draw.rect(self.screen, (0,0,0), self.screen.get_rect())
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)

    def handle_event(self, event):
        """ Swaps state to the Title Screen when a key is pressed. """
        if event.type == pygame.KEYDOWN:
            self.game.show_title()