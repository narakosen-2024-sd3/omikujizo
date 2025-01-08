# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false


from typing import Final, Literal

import pigpio

from ..gpio_number import GpioNumber
from .type.output_interface import IStaticOutput


class StaticOutput(IStaticOutput):
  def __init__(self, gpio_number: GpioNumber):
    self.__gpio_number: Final[GpioNumber] = gpio_number
    self.__gpio: Final[pigpio.pi] = pigpio.pi()
    self.__gpio.set_mode(self.__gpio_number.get_value(), pigpio.OUTPUT)

  def __set(self, level: Literal[0, 1]) -> None:
    gpio_number = self.__gpio_number.get_value()
    self.__gpio.write(gpio_number, level)

  def set_high(self) -> None:
    self.__set(1)

  def set_low(self) -> None:
    self.__set(0)
