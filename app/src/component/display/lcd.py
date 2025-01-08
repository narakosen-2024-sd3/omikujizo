from typing import Final

from src.lib.gpio.i2c.type.i2c_interface import II2c

from .type.lcd_interface import ILcd


class Lcd(ILcd):
  def __init__(self, i2c: II2c) -> None:
    self.__i2c: Final[II2c] = i2c

  def display(self, text: str) -> None:
    pass
