from typing import Final

from src.component.light.light_driver_interface import LightDriverInterface
from src.module.jewel.jewel_interface import JewelInterface


class Jewel(JewelInterface):
  def __init__(self, led: LightDriverInterface) -> None:
    self.__led: Final[LightDriverInterface] = led

  def turn_on(self) -> None:
    self.__led.turn_on()

  def turn_off(self) -> None:
    self.__led.turn_off()