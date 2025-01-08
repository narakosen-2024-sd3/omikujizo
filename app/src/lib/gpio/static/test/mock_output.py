import copy
from typing import Final

from ...gpio_number import GpioNumber
from ..type.output_interface import IStaticOutput


class MockStaticOutput(IStaticOutput):
  def __init__(self, gpio_number: GpioNumber) -> None:
    self.__histories: list[int] = []
    self.__gpio_number: Final[GpioNumber] = gpio_number

  def set_high(self) -> None:
    self.__histories.append(1)

  def set_low(self) -> None:
    self.__histories.append(0)

  def get_histories(self):
    return copy.deepcopy(self.__histories)
