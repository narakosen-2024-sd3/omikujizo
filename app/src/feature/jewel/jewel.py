from typing import Final

from src.component.light.type.light_interface import ILight

from .type.jewel_interface import IJewel


class Jewel(IJewel):
  def __init__(
    self,
    led: ILight,
  ) -> None:
    self.__led: Final[ILight] = led

  def turn_on(self) -> None:
    self.__led.turn_on()

  def turn_off(self) -> None:
    self.__led.turn_off()
