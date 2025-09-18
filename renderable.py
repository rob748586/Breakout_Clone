from abc import ABC, abstractmethod


class Renderable(ABC):
    """ Abstract class/interface for a renderable """
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def do_updates(self, timeslice):
        pass

