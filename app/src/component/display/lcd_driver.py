from typing import Final

from src.lib.gpio.i2c.type.i2c_interface import I2cInterface

from .type.lcd_driver_interface import LcdDriverInterface


class LcdDriver(LcdDriverInterface):
  def __init__(self, i2c: I2cInterface) -> None:
    self.__i2c: Final[I2cInterface] = i2c

  def display(self, text: str) -> None:
    pass
