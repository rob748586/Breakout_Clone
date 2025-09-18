import pygame

from renderable import Renderable


class ScoreBoard(Renderable):
    """ A Score Board renderable, displays score and lives at the top of the screen in game. """
    def __init__(self, game):
        super().__init__()
        """ Initialise the class """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.stats = game.stats

        self.update_scores()

    def update_scores(self):
        """ Updates the images for displayed score and lives. """
        self.score_image = pygame.font.SysFont(None, 24).render(f"Score: {self.stats.score}", True, self.settings.text_colour)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.left = 8
        self.score_image_rect.top = 4

        self.lives_image = pygame.font.SysFont(None, 24).render(f"Lives: ", True,
                                                                self.settings.text_colour)
        self.lives_image_rect = self.score_image.get_rect()
        self.lives_image_rect.right = self.screen.get_rect().width - 24
        self.lives_image_rect.top = 4

    def do_updates(self, timeslice):
        pass

    def render(self):
        """ Render the Score Board. """
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.lives_image, self.lives_image_rect)

        for n in range(self.stats.lives):
            pygame.draw.circle(self.screen, self.settings.ball_colour, (self.screen.get_rect().width - 8 - 15 * n, 14), 7, 0 )
            pygame.draw.circle(self.screen, self.settings.ball_outline_colour, (self.screen.get_rect().width - 8 - 15 * n, 14), 7, 2)

        panel_height = 24
        pygame.draw.rect(self.screen, self.settings.text_colour, pygame.Rect(0, panel_height, self.screen.get_rect().width, self.settings.border_top - panel_height))