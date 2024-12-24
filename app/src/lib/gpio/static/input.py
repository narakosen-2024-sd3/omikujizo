# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

from typing import Final

import pigpio

from ..gpio_number import GpioNumber
from .input_interface import StaticInputInterface
from .logic_level import LogicLevel


class StaticInputWrapper(StaticInputInterface):
  def __init__(self, gpio_number: GpioNumber):
    self.__gpio_number: Final[GpioNumber] = gpio_number
    self.__gpio: Final[pigpio.pi] = pigpio.pi()
    self.__gpio.set_mode(self.__gpio_number.get_value(), pigpio.INPUT)

  def read(self) -> LogicLevel:
    gpio_number = self.__gpio_number.get_value()
    level = self.__gpio.read(gpio_number)
    if level == 1:
      return LogicLevel("HIGH")
    if level == 0:
      return LogicLevel("LOW")

    raise RuntimeError()
