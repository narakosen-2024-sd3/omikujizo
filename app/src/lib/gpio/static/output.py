# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false


from typing import Final

import pigpio

from ..value.gpio_number import GpioNumber
from .type.output_interface import StaticOutputInterface
from .value.logic_level import LogicLevel


class StaticOutputWrapper(StaticOutputInterface):
  def __init__(self, gpio_number: GpioNumber):
    self.__gpio_number: Final[GpioNumber] = gpio_number
    self.__gpio: Final[pigpio.pi] = pigpio.pi()
    self.__gpio.set_mode(self.__gpio_number.get_value(), pigpio.OUTPUT)

  def set(self, logic_level: LogicLevel) -> None:
    gpio_number = self.__gpio_number.get_value()
    level = 1 if logic_level.is_high() else 0
    self.__gpio.write(gpio_number, level)
