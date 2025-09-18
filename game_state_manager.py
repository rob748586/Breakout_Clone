from game_state import GameStateBase

class GameStateManager:
    """ State machine to handle events, rendering and updates maintaining the current game state."""
    def __init__(self):
        """ Initialise Object """
        self.state_stack = []

    def push_state(self, state: GameStateBase):
        """ push the state to the top of the stack """
        self.state_stack.append(state)
        self.state_stack[-1].on_create()

    def pop_state(self):
        """ Remove the uppermost state if stack not empty. """
        if self.is_empty():
            return None

        self.state_stack[-1].on_destroy()
        return self.state_stack.pop()

    def do_updates(self, time_delta):
        """ Invoke the do_updates method on the active state. """
        if not self.is_empty():
            self.state_stack[-1].do_updates(time_delta)

    def do_render(self):
        """ Invoke the render method on the active state. """
        if not self.is_empty():
            self.state_stack[-1].render()

    def handle_event(self, event):
        """ Invoke the handle events method on the active state. """
        if not self.is_empty():
            self.state_stack[-1].handle_event(event)

    def is_empty(self):
        """ Returns true if no states are in the stack, False otherwise. """
        if len(self.state_stack) == 0:
            return True

        return False