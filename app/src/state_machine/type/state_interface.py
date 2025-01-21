from typing import Callable, Protocol

from ..state_label import StateLabel
from .disposable_interface import IDisposable

type EventHandler = Callable[[StateLabel], None]


class IState(Protocol):
  def entry(self) -> None:
    raise NotImplementedError()

  def do(self) -> None:
    raise NotImplementedError()

  def exit(self) -> None:
    raise NotImplementedError()

  def subscribe_state_change_event(self, handler: EventHandler) -> IDisposable:
    raise NotImplementedError()
