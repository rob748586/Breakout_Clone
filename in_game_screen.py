from random import randint

import pygame.draw
from pygame import Vector2

from brick import Brick
from game_state import GameStateBase
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

class InGameScreen(GameStateBase):
    def __init__(self, game):
        """ Initialise the class """
        super().__init__()
        self.screen = game.screen
        self.state_manager = game.state_manager
        self.settings = game.settings
        self.game = game
        self.scoreboard = ScoreBoard(game)
        self.stats = game.stats
        self.stats.reset()

    def on_create(self):
        """ Update the scoreboard and create all in game objects """
        self.scoreboard.update_scores()
        self.paddle = Paddle(self.screen, self.settings)
        self.ball = Ball(self.game, self.paddle.position + Vector2(0, -40))
        self.bricks = []

        for y in range(1, 8):
            for x in range(1, 6):
                dx = x + 0.5 if y % 2 == 1 else x
                dy = y + 1
                self.bricks.append (Brick(self.game, Vector2(dx * self.settings.brick_width, self.settings.border_top + dy * self.settings.brick_height), randint(1,4)))

    def on_destroy(self):
        pass

    def test_if_ball_left_screen(self):
        """ Test if the ball has left the screen on the bottom """
        if self.ball.position.y > self.screen.get_rect().height + 100:
            self.ball.reset_ball()
            self.stats.lives -= 1
            self.scoreboard.update_scores()

            if self.stats.lives < 0:
                self.game.lose_screen()

    def handle_event(self, event):
        """ Call Paddle's handle event method to parse input. """
        self.paddle.handle_event(event)

    def test_if_all_bricks_destroyed(self):
        """ Check if all bricks were destroyed, displaying the win screen if true. """
        if len(self.bricks) == 0:
            self.game.win_screen()

    def brick_hit(self, brick):
        """ Handle ball collided with brick, bounce ball, update score and test if brick destroyed. """
        self.ball.brick_bounce(brick)
        self.stats.score += 25
        self.scoreboard.update_scores()

        brick.hits_to_destroy -= 1

        if brick.hits_to_destroy <= 0:
            self.bricks.remove(brick)

    def do_updates(self, time_delta):
        """ Perform update on all in game objects. """
        self.paddle.do_updates(time_delta)
        self.ball.do_updates(time_delta)

        for brick in self.bricks:
            brick.do_updates(time_delta)

        if pygame.sprite.collide_rect(self.paddle, self.ball):
            self.ball.paddle_bounce_at(self.paddle.position)

        for brick in self.bricks:
            if pygame.sprite.collide_rect(brick, self.ball):
                self.brick_hit(brick)

        self.test_if_all_bricks_destroyed()
        self.test_if_ball_left_screen()

    def render(self):
        pygame.draw.rect(self.screen, (0,0,0), self.screen.get_rect())
        self.scoreboard.render()

        self.paddle.render()
        self.ball.render()

        for brick in self.bricks:
            brick.render()