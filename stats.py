class Stats:
    """ Stats tracked by the game. """
    def __init__(self):
        """ Initialise the class """
        self.score = 0
        self.lives = 2

    def reset(self):
        """ Reset the score and lives for a new game """
        self.score = 0
        self.lives = 2