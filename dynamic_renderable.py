from abc import abstractmethod

from renderable import Renderable

class DynamicRenderable(Renderable):
    """ Abstract base class/interface for Renderables that require per frame updates and events. """
    @abstractmethod
    def do_updates(self, time_delta):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass