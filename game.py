import pygame
from game_state_manager import GameStateManager
from in_game_screen import InGameScreen
from settings import Settings
from stats import Stats
from title_screen import Title_Screen
from win_lose_screen import WinLoseScreen

class Game:
    def __init__(self):
        """ Initialise the class. """
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.state_manager = GameStateManager()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = Stats()

        self.show_title()

    async def run(self):
        """ Main game loop. """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                if event.type == pygame.QUIT:
                    running = False
                    break

                self.state_manager.handle_event(event)

            if running:
                self.state_manager.do_updates(1.0 / 60)
                self.state_manager.do_render()

                pygame.display.flip()
                self.clock.tick(60)

        pygame.quit()

    def start_game(self):
        """ Display the game. """
        self.state_manager.pop_state()
        self.state_manager.push_state(InGameScreen(self))

    def show_title(self):
        """ Display the Title screen. """
        title_screen = Title_Screen(self)
        self.state_manager.push_state(title_screen)

    def win_screen(self):
        """ Display the You Win screen. """
        win_screen = WinLoseScreen(self, "You Win !!!")
        self.state_manager.pop_state()
        self.state_manager.push_state(win_screen)

    def lose_screen(self):
        """ Disply the You Lose screen. """
        win_screen = WinLoseScreen(self, "You Lose !!!")
        self.state_manager.pop_state()
        self.state_manager.push_state(win_screen)


