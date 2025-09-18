import pygame

from dynamic_renderable import DynamicRenderable


class Paddle(DynamicRenderable):
    def __init__(self, screen, settings):
        """ Initialise the class"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.colour = settings.paddle_colour
        self.outline_colour = settings.paddle_outline_colour
        self.movement_direction = 0
        self.move_speed = settings.paddle_move_speed
        self.rect = pygame.Rect(0, 0, settings.paddle_width, settings.paddle_height)

        position = pygame.Vector2(screen.get_rect().centerx, screen.get_rect().height - 50)
        self.rect.centerx = position.x
        self.rect.centery = position.y
        self.position = position

    def render(self):
        """ Render the paddle to screen. """
        pygame.draw.rect(self.screen, self.colour, self.rect, 0, self.settings.outline_rounding)
        pygame.draw.rect(self.screen, self.outline_colour, self.rect, self.settings.outline_width, self.settings.outline_rounding)

    def handle_event(self, event):
        """ Handle input events for the paddle. """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movement_direction = -1
            if event.key == pygame.K_RIGHT:
                self.movement_direction = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.movement_direction == -1:
                self.movement_direction = 0
            if event.key == pygame.K_RIGHT and self.movement_direction == 1:
                self.movement_direction = 0

    def do_updates(self, time_delta):
        """ Move the paddle according to inputs. """
        if self.movement_direction > 0:
            if (self.position.x + self.movement_direction * self.move_speed * time_delta < self.screen.get_rect().width - self.rect.width / 2):
                self.position.x += self.movement_direction * self.move_speed * time_delta

        if self.movement_direction < 0:
            if self.position.x + self.movement_direction * self.move_speed * time_delta> self.rect.width / 2:
                self.position.x += self.movement_direction * self.move_speed * time_delta

        self.rect.centerx = self.position.x