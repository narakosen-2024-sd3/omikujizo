from typing import Literal

from ..type.input_interface import IStaticInput


class MockStaticInput(IStaticInput):
  def __init__(self) -> None:
    self.__level: Literal[0, 1] = 0

  def is_high(self) -> bool:
    return self.__level == 1

  def is_low(self) -> bool:
    return self.__level == 0

  def set_level(self, level: Literal[0, 1]) -> None:
    self.__level = level
