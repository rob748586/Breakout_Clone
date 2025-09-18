import pygame.draw

from dynamic_renderable import DynamicRenderable

class Brick(DynamicRenderable):
    def __init__(self, game, position, hits_to_destroy):
        """ Initialise the class. """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.stats = game.stats
        self.rect = pygame.Rect(0, 0, self.settings.brick_width, self.settings.brick_height)
        self.rect.centerx = position.x
        self.rect.centery = position.y
        self.position = position
        self.hits_to_destroy = hits_to_destroy

    def render(self):
        """ Render the Brick. """
        pygame.draw.rect(self.screen, self.settings.brick_colour[self.hits_to_destroy], self.rect, 0, self.settings.outline_rounding)
        pygame.draw.rect(self.screen, self.settings.brick_outline_colour[self.hits_to_destroy], self.rect, self.settings.brick_outline_width, self.settings.outline_rounding)

    def do_updates(self, time_delta):
        pass

    def handle_event(self, event):
        pass
