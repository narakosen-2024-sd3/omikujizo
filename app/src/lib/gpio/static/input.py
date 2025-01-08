# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

from typing import Final, Literal

import pigpio

from ..gpio_number import GpioNumber
from .type.input_interface import IStaticInput


class StaticInput(IStaticInput):
  def __init__(self, gpio_number: GpioNumber):
    self.__gpio_number: Final[GpioNumber] = gpio_number
    self.__gpio: Final[pigpio.pi] = pigpio.pi()
    self.__gpio.set_mode(self.__gpio_number.get_value(), pigpio.INPUT)

  def __read(self) -> Literal[0, 1]:
    gpio_number = self.__gpio_number.get_value()
    level = self.__gpio.read(gpio_number)

    if not (level == 0 or level == 1):
      raise RuntimeError()

    return level

  def is_high(self) -> bool:
    return self.__read() == 1

  def is_low(self) -> bool:
    return self.__read() == 0
