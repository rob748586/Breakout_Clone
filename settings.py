class Settings:
    """ Centralised settings class with member variables related to rendering, movement and display. """
    def __init__(self):
        """ Initialse member variables. """
        self.outline_width = 3
        self.outline_rounding = 12

        self.brick_width = 125
        self.brick_height = 40
        self.brick_outline_width = 2

        self.brick_colour = []
        self.brick_outline_colour = []

        self.text_colour = (55, 255, 55)

        self.border_top = 30

        for n in range(6):
            scaler = (n+1) * (1.0/6)
            self.brick_colour.append((55 * scaler, 255 * scaler, 55 * scaler))
            self.brick_outline_colour.append(self.brick_colour[n - 1 if n > 0 else 0])

        self.ball_colour = self.brick_colour[4]
        self.ball_outline_colour = self.brick_outline_colour[4]
        self.ball_size = 10
        self.ball_speed = 450

        self.paddle_colour = self.brick_colour[4]
        self.paddle_outline_colour = self.brick_outline_colour[4]
        self.paddle_width = 150
        self.paddle_height = 24
        self.paddle_move_speed = 600
        self.paddle_bounce_upper_bound = 50