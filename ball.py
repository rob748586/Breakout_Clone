import random
from math import copysign
import pygame
from pygame import Vector2

from dynamic_renderable import DynamicRenderable

class Ball(DynamicRenderable):
    """ Class for the ball. """
    def __init__(self, game, position : Vector2):
        """ Initialise the class. """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.size = self.settings.ball_size
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.position = position
                

        self.reset_ball()

    def reset_ball(self):
        """ Reset the position and assign a random direction to the ball. """
        randx = random.choice([-3,2, 2,3])
        direction = Vector2(randx, -(6 - abs(randx)))

        rect = self.screen.get_rect()
        self.position = Vector2(rect.width / 2, rect.height - 100)
        self.rect.centerx, self.rect.centery = self.position.x, self.position.y
        self.direction = direction.normalize()
        self.moving = False

        # set a timer to start the ball moving after a second
        pygame.time.set_timer(self.settings.START_BALL_EVENT, 1000, 1)

    def render(self):
        """ Render the Ball. """
        pygame.draw.circle(self.screen, self.settings.ball_colour, self.position, self.size, 0)
        pygame.draw.circle(self.screen, self.settings.ball_outline_colour, self.position, self.size, self.settings.outline_width)

    def edge_bounce_at(self, destination):
        """ Calculate and apply bounces at the edge of the screen """
        if destination.x <= 0:
            self.direction.x = copysign(self.direction.x, 1)

        if destination.x >= self.screen.get_rect().width - self.size:
            self.direction.x = copysign(self.direction.x, -1)

        if destination.y <= self.settings.border_top:
            self.direction.y = copysign(self.direction.y, 1)

        self.direction = self.direction.normalize()

    def paddle_bounce_at(self, position):
        """ Calculate and apply bounce off Paddle. """
        difference = self.position.x - position.x
        if difference < -self.settings.paddle_bounce_upper_bound:
            self.direction.x = -3
        elif difference > self.settings.paddle_bounce_upper_bound:
            self.direction.x = 3
        else:
            self.direction.x = copysign(2, self.direction.x)

        self.direction.y = -(6 - abs(self.direction.x))

        self.direction = self.direction.normalize()
        self.do_updates(1/60)

    def brick_bounce(self, brick):
        """ Calculate and apply bounce off Brick. """
        difference = brick.position - self.position
        if abs(difference.x) > self.settings.brick_width / 2  - 5:
            self.direction.x = copysign(self.direction.x, -1) if brick.position.x > self.position.x else copysign(self.direction.x, 1)

        if abs(difference.y) > self.settings.brick_height / 2 - 5:
            self.direction.y = copysign(self.direction.y, -1) if brick.position.y > self.position.y else copysign(self.direction.y, 1)

        self.direction = self.direction.normalize()

    def do_updates(self, time_delta):
        """ If the ball is moving, update the position of the ball and test for collisions with the screen boundary, bouncing if required. """

        if self.moving:
            destination = self.position + self.direction * self.settings.ball_speed * time_delta

            if destination.x > 0 and destination.x < self.screen.get_rect().width and \
            destination.y > self.settings.border_top:
                self.position += self.direction * self.settings.ball_speed * time_delta
            else:
                self.edge_bounce_at(destination)

            self.rect.centerx, self.rect.centery = self.position.x, self.position.y

    def handle_event(self, event):
        if event.type == self.settings.START_BALL_EVENT:
            self.moving = True