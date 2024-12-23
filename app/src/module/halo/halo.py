from typing import Final

from src.component.light.light_driver_interface import LightDriverInterface
from src.lib.time.sleep_interface import SleepInterface
from src.module.halo.halo_interface import HaloInterface


class Halo(HaloInterface):
  def __init__(
    self,
    tape_light: LightDriverInterface,
    sleep: SleepInterface,
  ) -> None:
    self.__tape_light: Final[LightDriverInterface] = tape_light
    self.__sleep: Final[SleepInterface] = sleep

  def turn_on(self) -> None:
    self.__tape_light.turn_on()

  def turn_off(self) -> None:
    self.__tape_light.turn_off()

  def perform_special(self) -> None:
    for _ in range(10):
      self.__tape_light.turn_on()
      self.__sleep.sleep(0.25)
      self.__tape_light.turn_off()
      self.__sleep.sleep(0.25)
