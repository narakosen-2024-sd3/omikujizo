from .state_factory import StateFactory
from .state_label import StateLabel
from .type.disposable_interface import IDisposable
from .type.state_interface import IState


class StateMachine:
  def __init__(self, initial_state_label: StateLabel) -> None:
    self.__current_state: IState = StateFactory.create_state(initial_state_label)
    self.__subscription: IDisposable = (
      self.__current_state.subscribe_state_change_event(self.on_state_changed)
    )

  def on_state_changed(self, state_label: StateLabel) -> None:
    self.__subscription.dispose()
    self.__current_state.exit()

    self.__current_state = StateFactory.create_state(state_label)
    self.__subscription = self.__current_state.subscribe_state_change_event(
      self.on_state_changed
    )
    self.__current_state.entry()

  def dispose(self) -> None:
    self.__subscription.dispose()
