from src.lib.gpio.static.logic_level import LogicLevel
from src.lib.gpio.static.output_interface import StaticOutputInterface

from .light_driver_interface import LightDriverInterface


class LedDriver(LightDriverInterface):
  def __init__(self, anode_pin: StaticOutputInterface) -> None:
    self.__anode_pin = anode_pin

  def turn_on(self) -> None:
    self.__anode_pin.set(LogicLevel("HIGH"))

  def turn_off(self) -> None:
    self.__anode_pin.set(LogicLevel("LOW"))
