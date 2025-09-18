from abc import ABC, abstractmethod

class GameStateBase(ABC):
    """ Abstract base class/interface for game states. """
    @abstractmethod
    def on_create(self):
        pass

    @abstractmethod
    def on_destroy(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def do_updates(self, time_delta):
        pass

    @abstractmethod
    def render(self):
        pass