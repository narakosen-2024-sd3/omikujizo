from typing import Callable

from .type.disposable_interface import IDisposable


class Disposable(IDisposable):
  def __init__(self, func: Callable[[], None]) -> None:
    self.__func = func

  def dispose(self) -> None:
    self.__func()
