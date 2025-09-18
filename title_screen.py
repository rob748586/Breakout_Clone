import pygame

from game_state import GameStateBase


class Title_Screen(GameStateBase):
    """ The Title Screen Game State """
    def __init__(self, game):
        """ Initialise the object. """
        super().__init__()
        self.screen = game.screen
        self.state_manager = game.state_manager
        self.settings = game.settings
        self.game = game

    def on_create(self):
        """ Create the Title and prompt to press any key to continue text. """
        self.title = pygame.font.SysFont(None, 48).render("Break-out Clone", True, self.settings.text_colour)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = self.screen.get_rect().width / 2
        self.title_rect.centery = self.screen.get_rect().height / 2 - 10

        self.subtitle = pygame.font.SysFont(None, 24).render("Press any key to continue...", True, self.settings.text_colour)
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.centerx = self.screen.get_rect().width / 2
        self.subtitle_rect.centery = self.screen.get_rect().height / 2 + 20

    def on_destroy(self):
        pass

    def do_updates(self, time_delta):
        pass

    def handle_event(self, event):
        """ If a key is pressed, switch state to the game. """
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_ESCAPE:
                self.game.start_game()

    def render(self):
        """ Render the Title and prompt to screen. """
        pygame.draw.rect(self.screen, (0, 0, 0), self.screen.get_rect())
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)