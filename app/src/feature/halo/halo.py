from typing import Final

from src.component.light.type.light_interface import ILight
from src.lib.time.type.sleep_interface import ISleep

from .type.halo_interface import IHalo


class Halo(IHalo):
  def __init__(
    self,
    tape_light: ILight,
    sleep: ISleep,
  ) -> None:
    self.__tape_light: Final[ILight] = tape_light
    self.__sleep: Final[ISleep] = sleep

  def turn_on(self) -> None:
    self.__tape_light.turn_on()

  def turn_off(self) -> None:
    self.__tape_light.turn_off()

  async def perform_special(self) -> None:
    for _ in range(10):
      self.__tape_light.turn_on()
      await self.__sleep.sleep(0.25)
      self.__tape_light.turn_off()
      await self.__sleep.sleep(0.25)
